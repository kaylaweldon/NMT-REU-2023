# this code conveys the difference between distance measured by LBS
# vs distance as measured in Euclidean space. 

library(HilbertCurve)
library(circlize)
library(IRanges)

# adjust the range (0 will give a range of 10...)
range <- 40
x <- range / 2

# the side length, in cm, of one cell
scale <- 1.5

# the max disance from user in real space, represented by a circle
max_euclidean_distance <- 10

# a table of ranges at whose each center lies a user
ir <- IRanges(start = c(0, 38 - x, 90 - x, 155 - x, 230 - x),
         end = c(10, 48 + x, 100 + x, 165 + x, 240 + x))

# construction of the hilbert curve
hc1 <- HilbertCurve(0, 255, level = 4, arrow = TRUE,
        reference = TRUE, padding = unit(6, "cm"))

# construction of the area searched by the lbs
hc_rect(hc1, ir, gp = gpar(fill = rand_color(length(ir), transparency = 0.6)))

# visualization of the max Euclidean distance
hc_points(hc1, x1 = c(5, 43, 95, 160, 235), x2 = c(5, 43, 95, 160, 235),
        np = 1, shape = "circle",
        size = unit(scale * max_euclidean_distance, "cm"))

# labels indicating where a user is located
hc_text(hc1, ir, labels = c("a", "b", "c", "d", "e"),
        gp = gpar(fontsize = 33, col = "black", font = 2))
