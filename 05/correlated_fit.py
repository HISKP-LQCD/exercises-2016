#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse
import sys

import matplotlib.pyplot as pl
import numpy as np
import scipy.optimize as op


def dandify_axes(ax, legend=False):
    ax.grid(True)
    ax.margins(0.05)
    if legend:
        ax.legend(loc='best')


def dandify_figure(fig):
    fig.tight_layout()


def f(t, a):
    return np.concatenate([t, a * t**3])


def make_chi_sq(z, cov):
    cov_inv = cov**-1

    def chi_sq(param):
        t = param[:4]
        a = param[-1]
        z_minus_f = z - f(t, a)

        a = z_minus_f.transpose()
        b = cov_inv
        c = z_minus_f

        return a.dot(b).dot(c)[0, 0]

    def chi_sq_gradient(param):
        t = param[:4]
        a = param[-1]
        z_minus_f = z - f(t, a)

    return chi_sq


def perform_fit(z, initial_guess, cov):
    chi_sq = make_chi_sq(z, cov)
    print(initial_guess)
    print(chi_sq(initial_guess))
    result = op.minimize(chi_sq, initial_guess)
    print(result)

    return result.x[-1]


def main():
    options = _parse_args()

    # Read in the data.
    data = np.genfromtxt('data.tsv')
    y_val = data[:, 0]
    y_err = data[:, 1]
    x_val = data[:, 2]
    x_err = data[:, 3]
    rho = data[:, 4]

    print('Data:')
    print(data)

    cov_xx = np.diag(x_err**2)
    cov_yy = np.diag(y_err**2)
    cov_xy = np.diag(rho * x_err * y_err)

    cov = np.bmat([[cov_xx, cov_xy], [cov_xy, cov_yy]])
    print('Covariance matrix:')

    print(cov)
    
    z_val = np.concatenate([x_val, y_val])

    initial_guess = np.concatenate([x_val, [0.2]])
    a_val = perform_fit(z_val, initial_guess, cov)

    x = np.linspace(np.min(x_val), np.max(x_val), 100)
    y = a_val * x**3

    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.errorbar(x_val, y_val, xerr=x_err, yerr=y_err, marker='+', linestyle='none')
    ax.plot(x, y)

    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    dandify_axes(ax)
    dandify_figure(fig)
    fig.savefig('raw_data.pdf')
    fig.savefig('raw_data.png')


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
