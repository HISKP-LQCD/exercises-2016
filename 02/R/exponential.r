#!/usr/bin/Rscript

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

box_muller_alternative_2 = function() {
    # Sample from the exponential distribution until a suitable `y2` has been
    # found.
    repeat {
        y1 = rexp(1)
        y2 = rexp(1)

        if (y2 > (1 - y1)^2 / 2) {
            break;
        }
    }

    # Randomly determine the sign and return that value.
    u = runif(1)
    x = sign(2 * u - 1) * y1
    return(x)
}

# Draw a bunch of samples
samples = replicate(10000, box_muller_alternative_2())

# Make a quantile-quantile plot which the actual against the theoretical
# quantiles. That should quickly tell whether the resulting numbers are sampled
# from a normal distribution.
qqnorm(samples)
lines(c(-4, 4), c(-4, 4))
grid()
