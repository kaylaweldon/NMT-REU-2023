#must install the following packages
library(HilbertCurve)
library(circlize)
library(IRanges)
set.seed(12345)

# range table to be used below if wanted
x = sort(sample(100, 20))
s = x[1:10*2 - 1]
e = x[1:10*2]
ir = IRanges(s, e)
ir


#Hilbert curve of degree 4
hc2 = HilbertCurve(1, 100, level = 4, reference = TRUE)

#Rotated Hilbert curve
hc3 = HilbertCurve(1, 50, level = 3, reference = TRUE, arrow = TRUE, start_from = "topleft", first_seg = "horizontal")

#Rainbow Hilbert curve
col = rainbow(100)
hc4 = HilbertCurve(1, 100, level = 5)
hc_points(hc4, x1 = 1:99, x2 = 2:100, np = 3, gp = gpar(col = col, fill = col))

#Hilbert curve of degree 3
hc1 = HilbertCurve(1, 100, level = 3, reference = TRUE)
# a range of points
hc_points(hc1, x1 = 10, x2 = 30, np = 5)
# a rectangle filling those points
hc_rect(hc1, x1 = 50, x2 = 60, gp = gpar(fill = "#FFFFF549"))
hc_rect(hc1, x1 = 10, x2 = 30, gp = gpar(fill = "#FF000080"))




