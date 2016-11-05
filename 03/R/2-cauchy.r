#!/usr/bin/Rscript
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

pdf = function(x) {
    1 / (pi * (1 + x^2))
}

inverse_cdf = function(u) {
    tan(pi * (u - 1/2))
}

bin_count = 50
samples_count = 100000

###############################################################################
#                           Inverse Function Method                           #
###############################################################################

# Plot the original function.
x_orig = seq(-5, 5, length.out=200)
y_orig = pdf(x_orig)
plot(x_orig, y_orig, type='l', main='Original PDF', xlab='x', ylab='y')

# Plot the inverse function.
u_inv_cdf = seq(0.02, 0.98, length.out=100)
x_inv_cdf = inverse_cdf(u_inv_cdf)
plot(u_inv_cdf, x_inv_cdf, type='l', main='Inverse CDF', xlab='u', ylab='x')

# Sample from uniform and transform it.
start = proc.time()
u = runif(samples_count)
x = inverse_cdf(u)
end = proc.time()
duration_inverse_cdf = end - start
cat('Time for Inverse Function:', duration_inverse_cdf, '\n')

# There is a complication that the resulting values span the whole real
# numbers. We cannot sensibly display that in a histogram. Therefore we need to
# limit the histogram. Just using `xlim` here does not suffice; it would just
# adjust the plotting window. We want to have the bins focussed in a sensible
# interval. R would complain if the bins do not cover all the values, so we
# need to select the interesting values as well.
selection = -5 < x & x < 5
hist(x[selection], breaks=seq(-5, 5, length.out=bin_count), freq=FALSE,
     main='Sampling with Inverse Function Method')

# By not using all data points, we effectively have sampled a different pdf.
# This means that the normalization is off, we need to correct for that.
factor = samples_count / sum(selection)
lines(x_orig, y_orig * factor, col='red')

###############################################################################
#                                Ratio Method                                 #
###############################################################################

start = proc.time()
x = rnorm(samples_count)
y = rnorm(samples_count)
z = x / y
end = proc.time()
duration_inverse_cdf = end - start
cat('Time for Ratio:', duration_inverse_cdf, '\n')

selection = -5 < z & z < 5
hist(z[selection], breaks=seq(-5, 5, length.out=bin_count), freq=FALSE,
     main='Sampling with Ratio Method')

factor = samples_count / sum(selection)
lines(x_orig, y_orig * factor, col='red')
