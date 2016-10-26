#!/usr/bin/Rscript
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

plotwitherror <- function(x, y, dy, col="black", ...) {
  plot(x=x, y=y, col=col, ...)
  arrows(x0=x, y0=y-dy, x1=x, y1=y+dy, length=0.01,
         angle=90, code=3, col=col)
}

myprint = function(varname, var) {
    cat(paste0(varname, ':', '\n'))
    print(var)
    cat('\n')
}

task2 = function() {
    n = c(1:10)

    A = matrix(data=c(1:20), nrow=2)

    myprint('A', A)

    A1 = A[1,]
    A2 = A[2,]

    mean1 = cumsum(A1) / c(1:length(A1))
    mean2 = cumsum(A2) / c(1:length(A2))

    myprint('n', n)
    myprint('mean1', mean1)
    myprint('mean2', mean2)

    result = t(rbind(n, mean1, mean2))
    myprint('result', result)

    write.table(result, '00-2-R-running_mean.tsv', row.names=FALSE, col.names=FALSE)
    write.table(A, '00-2-R-A.tsv', row.names=FALSE, col.names=FALSE)
}

expectation1 = function(n) {
    return(n)
}

expectation2 = function(n) {
    return(n + 1)
}

task3 = function() {
    result = read.table('00-2-R-running_mean.tsv')

    n = result$V1
    mean1 = result$V2
    mean2 = result$V3

    pdf('00-3-R-running_mean.pdf')
    plot(x=n, y=mean1)
    lines(x=n, y=expectation1(n))
    plot(x=n, y=mean2)
    lines(x=n, y=expectation2(n))
    dev.off()

    pdf('00-3-R-running_mean_withmodelerror.pdf')
    plotwitherror (x=n, y=mean1, dy=(mean1*0.1), ylim=c(0,12), xlab="n", ylab=expression('S'['odd']))
    lines(x=n, y=expectation1(n))

    plotwitherror (x=n, y=mean2, dy=(mean2*0.1), ylim=c(0,12), xlab="n", ylab=expression('S'['even']))
    lines(x=n, y=expectation2(n))
    dev.off()


    #dev.copy2pdf('00-3-R-running_mean.pdf')
}

task4 = function() {
    A = read.table('00-2-R-A.tsv')

    myprint('A', A)

    squared1 = t(A[1,])^2
    squared2 = t(A[2,])^2

    myprint('squared1', squared1)
    myprint('squared2', squared2)

    n = c(1:length(squared1))

    mean1 = cumsum(squared1) / n
    mean2 = cumsum(squared2) / n

    pdf('00-4-R-running_mean_square.pdf')
    plot(n, mean1)
    lines(n, (2*n + 1) * (2 * n - 1) / 3)
    plot(n, mean2)
    lines(n, 2*(n + 1) * (2 * n + 1) / 3)
    dev.off()

    myprint('mean1', mean1)
    myprint('mean2', mean2)
}

task5 = function() {
    k = c(1:10^4)
    r = sin(k)
    pdf('00-5-R-hist.pdf')
    hist(r)

    indices = which(r > 0)
    number_positive = length(indices)
    myprint('number_positive', number_positive)

    r[r < 0] = 0

    mean_of_positive = mean(r)
    myprint('mean_of_positive', mean_of_positive)
}

task2()
task3()
task4()
task5()
