library(HilbertCurve)

# Rainbow Hilbert curve that does not return to red,
# rather, its range is red to blue
col <- rainbow(150)
hc4 <- HilbertCurve(1, 100, level = 5)
hc_points(hc4, x1 = 1:99, x2 = 2:100, np = 3, gp = gpar(col = col, fill = col))
