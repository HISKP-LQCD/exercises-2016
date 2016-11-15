#!/usr/bin/Rscript
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

iterapply = function(start, func, length) {
    result = numeric(length)
    result[1] = start
    for (i in 2:length) {
        result[i] = func(result[i - 1])
    }
    return(result)
}

get_next_x = function(x, alpha) {
    epsilon = runif(1)
    return (alpha * x + (1 - alpha) * epsilon)
}

generate_series = function(alpha) {
    return (iterapply(0, function(x) { return (get_next_x(x, alpha)) }, 100000))
}

xs = generate_series(0.1)
hist(xs, freq=FALSE)

xs = generate_series(0.3)
hist(xs, freq=FALSE)

xs = generate_series(0.7)
hist(xs, freq=FALSE)

xs = generate_series(0.9)
hist(xs, freq=FALSE)
