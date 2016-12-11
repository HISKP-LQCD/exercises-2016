#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse
import sys

import matplotlib.pyplot as pl
import numpy as np
import scipy.optimize as op

import bootstrap

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

        a = z_minus_f
        b = cov_inv
        c = z_minus_f.transpose()
        ab = a.dot(b)

        result = ab.dot(c)[0, 0]

        return result

    def chi_sq_gradient(param):
        t = param[:4]
        a = param[-1]
        z_minus_f = z - f(t, a)

    return chi_sq

conv = {True: 0, False: 0}


def perform_fit(z, initial_guess, cov):
    chi_sq = make_chi_sq(z, cov)
    #print(initial_guess)
    result = op.minimize(chi_sq, initial_guess)
    conv[result.success] += 1
    print(result.success)
    print(chi_sq(result.x))
    #print(result)

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
    a_central = perform_fit(z_val, initial_guess, cov)

    x = np.linspace(np.min(x_val), np.max(x_val), 100)
    y = a_central * x**3

    s = np.linalg.cholesky(cov).transpose()
    a_dist = []
    y_fit_dist = []
    for sample in range(100):
        r = np.random.normal(0, 1, 8)
        z = s.dot(r) + z_val

        a = perform_fit(z, initial_guess, cov)

        y_fit = a * x**3

        a_dist.append(a)
        y_fit_dist.append(y_fit)

    a_val, a_err = bootstrap.average_and_std_arrays(a_dist)
    y_fit_val, y_fit_err = bootstrap.average_and_std_arrays(y_fit_dist)

    print(a_central, a_val, a_err)

    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.errorbar(x_val, y_val, xerr=x_err, yerr=y_err, marker='+', linestyle='none', color='blue')
    ax.fill_between(x, y + y_fit_err, y - y_fit_err, color='black', alpha=0.2)
    ax.plot(x, y, color='red')

    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    dandify_axes(ax)
    dandify_figure(fig)
    fig.savefig('raw_data.pdf')
    fig.savefig('raw_data.png')

    print(conv)


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
