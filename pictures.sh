#!/bin/bash
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

set -e
set -u
set -x

pdfseparate Rplots.pdf $1-%d.pdf

for pdf in ./$1-*.pdf
do
    out="${pdf%.pdf}.png"
    convert "$pdf" -size 500x500 "$out"
done
