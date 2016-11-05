#!/usr/bin/Rscript
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

bin_count = 50
samples_count = 100000

pdf = function(x) {
    sqrt(1/x - log(1 - x))
}

gm = function(x) {
    4 / (pi * sqrt(x * (1 - x)))
}

# Plot the original function.
x_orig = seq(0.01, 0.99, length.out=200)
y_orig = pdf(x_orig)
plot(x_orig, y_orig, type='l', main='Original PDF', xlab='x', ylab='y',
     col='red')

# Also plot the majorizing function.
y = gm(x_orig)
lines(x_orig, y)

inverse_cdf = function(u) {
    sin(pi * u / 2)^2
}

u = runif(samples_count)
x = inverse_cdf(u)

u2 = runif(samples_count)
idx = u2 < pdf(x) / gm(x)
accepted = x[idx]

hist(accepted, breaks=bin_count, freq=FALSE)

# The pdf above needs to be normalized, on the problem/solution set the
# normalization is given as this particular magic number.
lines(x_orig, y_orig / 2.32812, col='red')
