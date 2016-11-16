#!/usr/bin/Rscript
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

data = read.table('weather.csv', header = TRUE, sep = ',', quote = "",
                  skip = 1, stringsAsFactors = FALSE)

years = data$Year[1:136]
temps = data[1:136, 2:13]

means = rowMeans(temps)

plot(years, means)

# Linear fit.
model = lm(means ~ years)

summary(model)
str(model)
