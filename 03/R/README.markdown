# Week 3

## Three Ways to Sample

### Inverse Function Method

First we take a look at the original pdf given:

![](plots-1-1.png)

The inverse cdf looks like this:

![](plots-1-2.png)

Sampling from a uniform distribution and transforming with the inverse gives us
sufficient agreement with the original pdf:

![](plots-1-3.png)

### Logistic Map

This is the map that we are going to use:

![](plots-1-4.png)

Iteratively applying it to the previous result gives us, for the first thousand
iterations, starting with `pi/4 - 0.1`:

![](plots-1-5.png)

I have chosen this number because it is not a multiple of `pi` but still an
irrational number.

Again we obtain a nice distribution of the values:

![](plots-1-6.png)

### Tent Function

The tent function looks a bit like the logistic map:

![](plots-1-7.png)

Even when starting with an irrational number, we do not get very far:

![](plots-1-8.png)

Naturally, the resulting histogram is very skewed and clearly shows that the
tent function is not suitable:

![](plots-1-9.png)

### Timings

| Method | User | System | Wall |
| --- | --- | --- | --- |
| Inverse | 0.022 | 0 | 0.022 |
| Logistic | 0.206 | 0.001 | 0.209 |
| Tent | 0.698 | 0 | 0.708 |

One can see that the standard method of inverse cdf is the fastest here. The
tent function seems to be the slowest for some reason, perhaps because of the
branching `x <= 1/2`?

## Cauchy Distribution

The original pdf is the following:

![](plots-2-1.png)

### Inverse Function Method

The inverse cdf:

![](plots-2-2.png)

Sampling with that inverse cdf gives satisfactory results:

![](plots-2-3.png)

### Ratio Method

The ratio method also gives good looking results:

![](plots-2-4.png)

### Timings

| Method | User | System | Wall |
| --- | --- | --- | --- |
| Inverse | 0.024 | 0 | 0.024 |
| Ratio | 0.021 | 0 | 0.021 |

Both methods have comparable complexity.

<!-- vim: set spell tw=79 : -->
