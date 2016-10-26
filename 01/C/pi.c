// Copyright © 2016 Martin Ueding <dev@martin-ueding.de>

// Computation of pi using the standard Monte Carlo method. Uses OpenMP for
// acceleration.

// Compile with:
//
// gcc -Wall -Wpedantic -fopenmp -O3 pi.c -o pi

#include <omp.h>

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    uint_fast64_t trials = 1e9;
    uint_fast64_t accepted = 0;

#pragma omp parallel reduction(+ : accepted)
    {
        unsigned int seed = omp_get_thread_num();
#pragma omp for
        for (uint_fast64_t i = 0; i < trials; i++) {
            double x = (double)rand_r(&seed) / RAND_MAX;
            double y = (double)rand_r(&seed) / RAND_MAX;
            double radius_squared = x * x + y * y;
            if (radius_squared < 1.0) {
                ++accepted;
            }
        }
    }

    printf("π = %.20g\n", 4.0 * accepted / trials);

    return 0;
}
