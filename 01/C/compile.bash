#!/bin/bash
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

gcc -Wall -Wpedantic -fopenmp -O3 pi.c -o pi
