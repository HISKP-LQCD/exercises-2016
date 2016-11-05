#!/usr/bin/Rscript
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

orig_pdf = function(x) {
    1 / sqrt(x * (1 - x)) / pi
    # The `return` is not needed, the return value is the last expression which
    # has been evaluated.
}

bin_count = 50
samples_count = 100000

###############################################################################
#                     Method (a): Inverse Function Method                     #
###############################################################################

inverse_cdf = function(u) {
    1 - sin(1/2 * (pi - pi * u))^2
}

# Plot the original function.
x_orig = seq(0, 1, length.out=200)
y_orig = orig_pdf(x_orig)
plot(x_orig, y_orig, type='l', main='Original PDF', xlab='x', ylab='y')

# Plot the inverse function.
u_inv_cdf = seq(0, 1, length.out=100)
x_inv_cdf = inverse_cdf(u_inv_cdf)
plot(u_inv_cdf, x_inv_cdf, type='l', main='Inverse CDF', xlab='u', ylab='x')

# Sample from uniform, transform it and plot a histogram.
start = proc.time()
u = runif(samples_count)
x = inverse_cdf(u)
end = proc.time()
duration_inverse_cdf = end - start
hist(x, breaks=bin_count, freq=FALSE, main='Sampling with Inverse Function Method')
lines(x_orig, y_orig, col='red')

###############################################################################
#                          Method (b): Logistic Map                           #
###############################################################################

logistic_map = function(x) {
    4 * x * (1 - x)
}

iterapply = function(start, func, length) {
    result = numeric(length)
    result[1] = start
    for (i in 2:length) {
        result[i] = func(result[i - 1])
    }
    return(result)
}

x = seq(0, 1, length.out=200)
y = logistic_map(x)
plot(x, y, type='l', main='Logistic Map', xlab='x', ylab='y')

start = proc.time()
iterations = iterapply(pi/4 - 0.1, logistic_map, samples_count)
end = proc.time()
duration_logistic = end - start

plot(iterations[1:1000], main='Successive Applications of the Logistic Map')
hist(iterations, breaks=bin_count, freq=FALSE, main='Sampling with Logistic Map')
lines(x_orig, y_orig, col='red')

###############################################################################
#                          Method (c): Tent Function                          #
###############################################################################

tent = function(x) {
    result = numeric(length(x))
    idx1 = x <= 1/2
    idx2 = x > 1/2
    result[idx1] = 2 * x[idx1]
    result[idx2] = 2 * (1 - x[idx2])
    return(result)
}

x = seq(0, 1, length.out=200)
y = tent(x)
plot(x, y, type='l', main='Tent Function', xlab='x', ylab='y')

start = proc.time()
iterations = iterapply(pi/4 - 0.1, tent, samples_count)
end = proc.time()
duration_tent = end - start

plot(iterations[1:1000], main='Successive Applications of the Tent Function')
hist(iterations, breaks=bin_count, freq=FALSE, main='Sampling with Tent Function')
lines(x_orig, y_orig, col='red')

cat("Times; user, system, wall:\n")
cat("Inverse cdf:  ", duration_inverse_cdf, "\n")
cat("Logistic Map: ", duration_logistic, "\n")
cat("Tent:         ", duration_tent, "\n")
