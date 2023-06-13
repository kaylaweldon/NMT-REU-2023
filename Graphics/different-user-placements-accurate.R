# this code conveys the difference between distance measured by LBS
# vs distance as measured in Euclidean space.
#
# the thing that is really tricky here is the scale. I eyeballed it 
# by measuring a circle of 1.3 cm diameter to what appeared to be one cell

library(HilbertCurve)
library(circlize)
library(IRanges)

# the side length, in cm, of one cell
scale <- 1.3

# the max disance from user in real space, represented by a circle
max_euclidean_distance <- 5

# adjust the range,
#    a factor of 1 means LBS searches 1 unit for every euclidean unit
adjustment_factor <- 1
range <- ((max_euclidean_distance) / scale) * adjustment_factor
x <- range

# a table of ranges at whose each center lies a user
ir <- IRanges(start = c(0, 43 - x, 95 - x, 160 - x, 235 - x),
         end = c(0 + x, 43 + x, 95 + x, 160 + x, 235 + x))

# construction of the hilbert curve
hc1 <- HilbertCurve(0, 255, level = 4, arrow = TRUE,
        start_from = "bottomleft", first_seg = "horizontal",
        reference = TRUE, padding = unit(6, "cm"))

# construction of the area searched by the lbs
hc_rect(hc1, ir, gp = gpar(fill = rand_color(length(ir), transparency = 0.6)))
hc_points(hc1, ir, np = 2, shape = "square")


# visualization of the max Euclidean distance
hc_points(hc1, x1 = c(5, 43, 95, 160, 235), x2 = c(5, 43, 95, 160, 235),
        np = 1, shape = "circle",
        size = unit(2 * scale * max_euclidean_distance, "cm"))

# test the unit of one cell
hc_points(hc1, x1 = 0, x2 = 4, np = 1, size = unit(1.3, "cm"), shape = "circle")
hc_points(hc1, x1 = 0, x2 = 10, np = 2, shape = "square")

# labels indicating where a user is located
hc_text(hc1, ir, labels = c("a", "b", "c", "d", "e"),
        gp = gpar(fontsize = 33, col = "black", font = 2))


# area of one cell times total cells searched, including user cell
LBS_search_area <- (scale^2) * (2 * range + 1)

# area of a circle of radius max distance
euclid_search_area <- pi * (max_euclidean_distance ^ 2)

LBS_to_euclid_area_percentage <- 100 * (LBS_search_area / euclid_search_area)


# display areas
cat(LBS_search_area, "\n")
cat(euclid_search_area, "\n")

# display ratio
cat(LBS_to_euclid_area_percentage, "\n")

