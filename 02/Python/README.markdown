# Uniform Number Generation

This program generates the numbers as defined on the exercise sheet. A lot of
samples are taken and put into a histogram. Together with the expected
uncertainty, this is in the left plot.

On the right there is a distribution of the residuals, the difference to 10000
in each bin. It should resemble a standard normal distribution.

![](uniform.png)

Run this with:

    ./uniform.py

If you want to choose the parameters, you can do so using command line options:

    ./uniform.py --digits DIGITS --samples SAMPLES
