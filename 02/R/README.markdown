# Box-Muller Method Alternatives

## Acceptance Rate

The first algorithm contains an accept/reject step. It is asked to compute the
average number of trials, this is related to the acceptance rate.

See the program `accept-reject.r` for an implementation. For 10000 numbers
generated, the average number of trials is given as 1.2722. Given that the
error is to be about 1%, this is in great agreement with the analytic
expectation of 1.27324. Derivation is the following:

![](analytic-part.png)

I have also implemented this example (although not explicitly asked, I guess).
It seems to produce sensible results, as can be seen in the QQ-plot:

![](qqplot1.png)

## Implementation of Second Alternative

The second alternative does the computation differently but still has an
accept-reject step in it. See `exponential.r` for the implementation.

As one can see in the QQ-plot, the results are also satisfactory:

![](qqplot2.png)

# Uniform Sampling on the Sphere

The uniform sampling on the unit circle (2-sphere) is implemented in
`sphere.r`. The results can be displayed in a straightforward way:

![](sphere-1.png)

For the unit sphere (3-sphere), it is not that easy. Just plotting `x` and `y`
in a scatter plot gives this:

![](sphere-2.png)

It is hard to tell whether this is correct. One would expect that the density
at the edges is higher but our eye is not at judging this quantitatively.

We can use the area preserving [Hammer-Aitoff
projection](https://en.wikipedia.org/wiki/Hammer_projection) to project the
surface of the 3-sphere onto a plane. Then it looks like this:

![](sphere-3.png)

Sampling in the bulk of an n-sphere is also possible by generating a new radius
and adjusting for the Jacobian of that dimension. The result for the bulk of a
2-sphere (disk) looks like this:

![](sphere-4.png)

Although we already know that makes little sense to plot the projection of 3D →
2D space by omitting the `z` component, this is a simple way to at least take a
look at the bulk of the 3D sampling:

![](sphere-5.png)

If one had a proper volume-to-area mapping, one could probably also make a nice
2D picture out of this.
