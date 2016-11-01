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


def myprint(name, variable):
    print()
    print(name + ':')
    print(variable)


def main():
    options = _parse_args()


    # Obtain the sufficient number of ones and zeros.
    zeros_ones = np.random.randint(0, 2, options.samples * options.digits)
    myprint('zeros_ones', zeros_ones)

    # Get the coefficients into the correct shape, also make them +1 and -1.
    coefficients = zeros_ones.reshape((options.samples, options.digits))
    coefficients = 2 * coefficients - 1
    myprint('coefficients', coefficients)

    # Get the $(1/2)^j$ style weights.
    weights = 0.5**np.arange(1, options.digits + 1)
    myprint('weights', weights) 

    # Apply the weights to the individual summands.
    weighted_summands = coefficients * weights
    myprint('weighted_summands', weighted_summands)

    # Then sum the summands to yield the resulting number $Y$.
    numbers = np.sum(weighted_summands, axis=1)
    myprint('numbers', numbers)

    # We expect an $1/\sqrt{N}$ like error distribution. The expected number of
    # elements in each bin of the histogram (using as many bins as there are
    # digits in the in the number) can be easily calculated. From this we
    # compute an error band to plot later on.
    y_span = np.linspace(-1.0, 1.0, 2)
    expected = options.samples / options.digits
    error = np.sqrt(expected)
    expected_span = np.ones(y_span.shape) * expected

    # Create a new figure.
    fig = pl.figure()

    # Add a subplot.
    ax = fig.add_subplot(1, 2, 1)

    # Plot the histogram of $Y$.
    values, edges, patches = ax.hist(numbers, bins=options.digits, label='Samples')

    # Add one and two standard deviations as lines to judge the jitter.
    ax.plot(y_span, expected_span, color='green', label='Expected')
    ax.plot(y_span, expected_span + error, color='red', label=r'$1 \sigma$')
    ax.plot(y_span, expected_span - error, color='red')
    ax.plot(y_span, expected_span + 2 * error, color='orange', label=r'$2 \sigma$')
    ax.plot(y_span, expected_span - 2 * error, color='orange')

    # Make the plot pretty.
    ax.set_title('Histogram of Generated Numbers')
    ax.set_xlabel('$Y$')
    ax.set_ylabel('Count')
    dandify_axes(ax)

    # Add another plot.
    ax = fig.add_subplot(1, 2, 2)

    # Make a histogram where the residuals (actual - expected) are divided by
    # the expected standard deviation. The result should be a standard normal
    # distribution.
    ax.hist((values - expected) / error)

    # Also make that plot pretty.
    ax.set_title('Distribution of Residuals')
    ax.set_xlabel(r'$\frac{\tilde{Y} - Y}{\sqrt{N}}$')
    ax.set_ylabel('Count')
    dandify_axes(ax)

    # Make the whole figure pretty and store it to disk.
    dandify_figure(fig)
    fig.savefig('uniform.pdf')
    fig.savefig('uniform.png')



def _parse_args():
    '''
    Parses the command line arguments.

    :return: Namespace with arguments.
    :rtype: Namespace
    '''
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--digits', type=int, default=100)
    parser.add_argument('--samples', type=int, default=1000000)
    options = parser.parse_args()

    return options


if __name__ == '__main__':
    main()
