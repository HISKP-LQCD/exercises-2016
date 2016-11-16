#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse
import itertools

import matplotlib.pyplot as pl
import numpy as np
import scipy.optimize as op
from scipy import stats


def dandify_axes(ax):
    ax.grid(True)
    ax.margins(0.05)
    ax.legend(loc='best')


def dandify_figure(fig):
    fig.tight_layout()


def poly0(x, a):
    return a * np.ones(x.shape)

def poly1(x, a, b):
    return poly0(x, a) + b * x

def poly2(x, a, b, c):
    return poly1(x, a, b) + c * x**2

def poly3(x, a, b, c, d):
    return poly2(x, a, b, c) + d * x**3


def main():
    options = _parse_args()

    data = np.loadtxt('weather.csv', skiprows=2, delimiter=',')
    years = data[:, 0]
    temps = data[:, 1:13]
    means = np.mean(temps, axis=1)
    stds = np.std(temps, axis=1) / np.sqrt(12)

    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.errorbar(years, means, stds, linestyle='none', marker='o', label='data')

    x = np.linspace(np.min(years), np.max(years), 200)

    print('| Degree | χ² | χ² / dof | p |')
    print('| --- | --- | --- | --- |')

    for func, degree in zip([poly0, poly1, poly2, poly3], itertools.count()):
        popt, pconv = op.curve_fit(func, years, means)

        y = func(x, *popt)
        ax.plot(x, y, label=str(func))

        residuals = means - func(years, *popt)
        chi_sq = np.sum(residuals**2 / stds**2)
        dof = len(years) - len(popt) - 1
        p_value = 1 - stats.chi2.cdf(chi_sq, dof)
        print('| {} | {:.4g} | {:.4g} | {:.4g} |'.format(degree, chi_sq, chi_sq/dof, p_value))

    ax.set_title('Weather Data Fit')
    ax.set_xlabel('Year')
    ax.set_ylabel('Temperature Deviation')
    dandify_axes(ax)
    dandify_figure(fig)
    fig.savefig('plot-weather-fit.pdf')
    fig.savefig('plot-weather-fit.png')



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
