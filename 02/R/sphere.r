#!/usr/bin/Rscript

# Copyright © 2016 Martin Ueding <dev@martin-ueding.de>
# Licensed under the MIT license.

rsurf = function(dim=3) {
    # Generate random vector components.
    x = rnorm(dim)

    # Normalize by the radius.
    r = sqrt(sum(x^2))
    y = x / r

    return(y)
}

rbulk = function(dim=3) {
    # Generate random vector components.
    x = rnorm(dim)

    # Normalize by the radius.
    r = sqrt(sum(x^2))
    x_normalized = x / r

    # Sample a new radius and adjust it for the Jacobian on that dimension.
    r_new = runif(1)^(1/dim)
    y = r_new * x_normalized

    return(y)
}

# Generate points and show them in a sensible fashion.

# 2D Surface.
samples_2d_surf = replicate(100, rsurf(2))
plot(samples_2d_surf[1,], samples_2d_surf[2,])

# 3D Surface.
samples_3d_surf = replicate(2000, rsurf(3))
x = samples_3d_surf[1,]
y = samples_3d_surf[2,]
z = samples_3d_surf[3,]

plot(x, y)

lambda = atan2(y, x)
r = sqrt(x^2 + y^2)
phi = atan2(z, r)

px = 2 * sqrt(2) * cos(phi) * sin(lambda/2) / sqrt(1 + cos(phi) * cos(lambda/2))
py = sqrt(2) * sin(phi) / sqrt(1 + cos(phi) * cos(lambda/2))

plot(px, py)


# 2D Bulk
samples_2d_bulk = replicate(2000, rbulk(2))
plot(samples_2d_bulk[1,], samples_2d_bulk[2,])

# 3D Bulk
samples_3d_bulk = replicate(2000, rbulk(3))
plot(samples_3d_bulk[1,], samples_3d_bulk[2,])
