#!/bin/bash
# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

pdfseparate Rplots.pdf Rplots-%d.pdf

for pdf in ./Rplots-*.pdf
do
    out="${pdf%.pdf}.png"
    convert "$pdf" -size 500x500 "$out"
done
