#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

import argparse

import matplotlib.pyplot as pl
import numpy as np
import scipy.optimize as op


def dandify_axes(ax):
    ax.grid(True)
    ax.margins(0.05)
    ax.legend(loc='best')


def dandify_figure(fig):
    fig.tight_layout()


def main():
    options = _parse_args()

    pi_4 = np.pi / 4

    # Obtain two random numbers for each iteration desired.
    sample = np.random.random_sample((options.iterations, 2))

    # Compute the radii by squaring all components and using `np.sum` to
    # generate a sum of the `x` and `y` compontents.
    radii_squared = np.sum(sample**2, axis=1)

    # Create an index array with all accepted points.
    accepted = radii_squared <= 1.0

    # Create an array which contains 0 or 1 depending on the acceptance step.
    result = np.zeros(radii_squared.shape)
    result[accepted] = 1

    # In order to obtain the standard deviation after a number of runs, we need
    # the mean value. We do this here using a cummulative sum. Squaring the
    # result does not make any difference *in this particular case*, but in
    # general that is needed.
    cumulative_sum = np.cumsum(result)
    cumulative_sum_sq = np.cumsum(result**2)
    n = np.arange(1, options.iterations + 1)

    # Using the cumulative sums we can compute a cumulative mean and
    # mean-squared. From those we can compute variance and standard error.
    mean = cumulative_sum / n
    mean_sq = cumulative_sum_sq / n
    variance = (mean_sq - mean**2) * n / (n - 1)
    standard_error = np.sqrt(variance / n)

    fig = pl.figure()

    ax1 = fig.add_subplot(1, 2, 1)
    ax1.fill_between(n, mean - standard_error, mean + standard_error, color='gray')
    ax1.plot(n, mean, color='black')
    ax1.plot((np.min(n), np.max(n)), (pi_4, pi_4), color='red', alpha=0.5)
    ax1.set_title('Result')
    ax1.set_xlabel('Iteration')
    ax1.set_ylabel(r'$\bar x$')
    dandify_axes(ax1)

    ax2 = fig.add_subplot(1, 2, 2)
    ax2.loglog(n, standard_error)
    ax2.loglog(n, np.sqrt(pi_4 * (1 - pi_4) / n))
    ax2.set_title('Significant Digits')
    ax2.set_xlabel('Iteration')
    ax2.set_ylabel('Standard Error')
    dandify_axes(ax2)

    dandify_figure(fig)
    fig.savefig('pi.pdf')


def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('iterations', type=int)
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
