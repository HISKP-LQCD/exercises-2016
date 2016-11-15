# Week 4

## 2. Pseudo Random Numbers

Depending on the value of α, you get different widths of the distribution:

![](plots-prng-1.png)
![](plots-prng-2.png)
![](plots-prng-3.png)
![](plots-prng-4.png)

## 3. Weather

I have solved this in one in Python, see [weather.py](weather.py). The data had
to be normalized first because there were `***` in there. Reading these into R
caused some troubles as well. I ended up deleting the first and last lines.

As one can see from the p-values, the quadratic fit is the best one:

| Degree | χ² | χ² / dof | p |
| --- | --- | --- | --- |
| 0 | 1.5e+03 | 11 | 0 |
| 1 | 3.9e+02 | 2.9 | 0 |
| 2 | 2.1e+02 | 1.6 | 8.6e-06 |
| 3 | 2.1e+02 | 1.6 | 2.5e-05 |

![](plot-weather-fit.png)
