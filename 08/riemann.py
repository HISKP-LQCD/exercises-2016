#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse

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


def f(x):
    return np.exp(-(x - 0.5)**2/2) / np.sqrt(2 * np.pi)


def main():
    options = _parse_args()

    x = np.random.random_sample(1000)
    u = np.array([0] + sorted(x) + [1])


    fu = f(u)
    summands = 0.5 * (u[1:] - u[:-1]) * (fu[1:] + fu[:-1])
    integral = np.sum(summands)

    print(integral)



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
