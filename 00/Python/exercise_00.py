#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

import matplotlib.pyplot as pl
import numpy as np
import scipy.optimize as op


def task_2():
    N = 10**1  # Only 10^1 for better separation in the plots.
    k_list = np.arange(1, N + 1)
    A = np.stack([2 * k_list - 1, 2 * k_list])

    print('A:')
    print(A)
    print()

    n_list = np.arange(1, N + 1)
    running_mean = np.row_stack(
        np.mean(A[:, :int(n)], axis=1) for n in n_list
    )

    print('running_mean:')
    print(running_mean)
    print()

    result = np.column_stack([n_list, running_mean])

    print('result:')
    print(result)
    print()

    np.savetxt('00-2-py-n.tsv', n_list)
    np.savetxt('00-2-py-A.tsv', A)
    np.savetxt('00-2-py-running_mean.tsv', result)


def expectation_1(n):
    return n


def expectation_2(n):
    return n + 1


def task_3():
    # Read the data back from the file.
    data = np.loadtxt('00-2-py-running_mean.tsv')
    n_list = data[:, 0]
    running_mean_1 = data[:, 1]
    running_mean_2 = data[:, 2]

    # Plot of the running means with expectation.
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(n_list, expectation_1(n_list), label='Expectation 1')
    ax.plot(n_list, expectation_2(n_list), label='Expectation 2')
    ax.plot(n_list, running_mean_1, label=r'$\mu_1$', linestyle='none', marker='o')
    ax.plot(n_list, running_mean_2, label=r'$\mu_2$', linestyle='none', marker='o')
    ax.grid(True)
    ax.legend(loc='best')
    ax.margins(0.05)
    ax.set_title('Running means')
    ax.set_xlabel(r'$n$')
    ax.set_ylabel(r'$\mu_i(n)$')
    fig.tight_layout()
    fig.savefig('00-3-py-running_mean.pdf')

    # Plot with error bars.
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(n_list, expectation_1(n_list), label='Expectation 1')
    ax.plot(n_list, expectation_2(n_list), label='Expectation 2')
    ax.errorbar(n_list, running_mean_1, yerr=0.1 * running_mean_1, label=r'$\mu_1$', linestyle='none', marker='o')
    ax.errorbar(n_list, running_mean_2, yerr=0.1 * running_mean_1, label=r'$\mu_2$', linestyle='none', marker='o')
    ax.grid(True)
    ax.legend(loc='best')
    ax.margins(0.05)
    ax.set_title('Running means')
    ax.set_xlabel(r'$n$')
    ax.set_ylabel(r'$\mu_i(n)$')
    fig.tight_layout()
    fig.savefig('00-3-py-running_mean_error.pdf')


def expectation_square_1(n):
    '''
    http://quiz.geeksforgeeks.org/sum-of-squares-of-even-and-odd-natural-numbers/
    '''
    return (2 * n + 1) * (2 * n - 1) / 3


def expectation_square_2(n):
    return 2 * (n + 1) * (2 * n + 1) / 3


def task_4():
    A = np.loadtxt('00-2-py-A.tsv')
    n_list = np.loadtxt('00-2-py-n.tsv')

    running_mean_squared = np.row_stack(
        np.mean(A[:, :int(n)]**2, axis=1) for n in n_list
    )

    running_mean_1 = running_mean_squared[:, 0]
    running_mean_2 = running_mean_squared[:, 1]

    # Plot of the running means with expectation.
    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(n_list, expectation_square_1(n_list), label='Expectation 1')
    ax.plot(n_list, expectation_square_2(n_list), label='Expectation 2')
    ax.plot(n_list, running_mean_1, label=r'$\mu_1^{(2)}$', linestyle='none', marker='o')
    ax.plot(n_list, running_mean_2, label=r'$\mu_2^{(2)}$', linestyle='none', marker='o')
    ax.grid(True)
    ax.legend(loc='best')
    ax.margins(0.05)
    ax.set_title('Running means')
    ax.set_xlabel(r'$n$')
    ax.set_ylabel(r'$\mu_i(n)^{(2)}$')
    fig.tight_layout()
    fig.savefig('00-4-py-running_mean_square.pdf')


def task_5():
    N = 10**4
    k = np.arange(1, N + 1)
    r = np.sin(k)

    fig = pl.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(r, bins=40)
    ax.set_xlabel(r'\sin(k)')
    ax.set_ylabel('Counts')
    fig.tight_layout()
    fig.savefig('00-5-py-hist.pdf')

    number_positive = (r > 0).sum()
    print('number_positive:', number_positive)

    fraction_positive = number_positive / N
    print('fraction_positive:', fraction_positive)

    r[r < 0] = 0

    mean_of_positive = np.mean(r)
    print('mean_of_positive:', mean_of_positive)


def main():
    task_2()
    task_3()
    task_4()
    task_5()


if __name__ == '__main__':
    main()
