library(HilbertCurve)

#Rainbow Hilbert curve
col <- rainbow(100)
hc4 <- HilbertCurve(1, 100, level = 5)
hc_points(hc4, x1 = 1:99, x2 = 2:100, np = 3, gp = gpar(col = col, fill = col))


n_points <- 100
gray_vals <- seq(0, 1, length.out = n_points)
col <- gray(gray_vals)

hc4 <- HilbertCurve(1, n_points, level = 5)
hc_points(hc4, x1 = 1:(n_points - 1), x2 = 2:n_points, np = 3, gp = gpar(col = col, fill = col))