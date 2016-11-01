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
        u = runif(1)
        v = runif(1)

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
