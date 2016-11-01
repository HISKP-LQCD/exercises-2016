#!/usr/bin/Rscript

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

myprint = function(varname, var) {
    cat(paste0(varname, ':', '\n'))
    print(var)
    cat('\n')
}

number_of_generations = function() {
    iterations = 0
    repeat {
        u = runif(1, min=-1, max=1)
        v = runif(1, min=-1, max=1)

        iterations = iterations + 1

        r_sq = u^2 + v^2

        if (r_sq <= 1) {
            break;
        }
    }

    return(iterations)
}

numbers = replicate(10000, number_of_generations())
myprint('numbers', numbers)

average_number = mean(numbers)
myprint('average_number', average_number)

# Define the function again, this time it returns an actual data type
box_muller_alternative_1 = function() {
    repeat {
        u = runif(1, min=-1, max=1)
        v = runif(1, min=-1, max=1)

        s = u^2 + v^2

        if (s <= 1) {
            break;
        }
    }

    z = sqrt(- 2 * log(s) / s)
    x1 = z * u
    x2 = z * v

    return(c(x1, x2))
}

# Draw a bunch of samples
samples = matrix(replicate(10000, box_muller_alternative_1()), nrow=1)

# Make a quantile-quantile plot which the actual against the theoretical
# quantiles. That should quickly tell whether the resulting numbers are sampled
# from a normal distribution.
qqnorm(samples)
lines(c(-4, 4), c(-4, 4))
grid()
