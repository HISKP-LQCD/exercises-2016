# Box-Muller Method Alternatives

## Acceptance Rate

The first algorithm contains an accept/reject step. It is asked to compute the
average number of trials, this is related to the acceptance rate.

TODO Analytic part

See the program `accept-reject.r` for an implementation. For 10000 numbers
generated, the average number of trials is given as 1.2722.

The QQ-plot looks reasonable:

![](qqplot1.png)

## Implementation of Second Alternative

The second alternative does the computation differently but still has an
accept-reject step in it. See `exponential.r` for the implementation.

As one can see in the QQ-plot, the results are not that good (or my
implementation is incorrect):

![](qqplot2.png)
