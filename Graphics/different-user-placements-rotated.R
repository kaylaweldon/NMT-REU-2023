# this code conveys the difference between distance measured by LBS
# vs distance as measured in Euclidean space. 

library(HilbertCurve)
library(circlize)
library(IRanges)

# the side length, in cm, of one cell
scale <- 1.5

# the max disance from user in real space, represented by a circle
max_euclidean_distance <- 10

# adjust the range
adjustment_factor <- 1
range <- (max_euclidean_distance / scale) * adjustment_factor
x <- range / 2

# a table of ranges at whose each center lies a user
ir <- IRanges(start = c(0, 43 - x, 95 - x, 160 - x, 235 - x),
         end = c(10, 43 + x, 95 + x, 160 + x, 235 + x))

# construction of the hilbert curve
hc1 <- HilbertCurve(0, 255, level = 4, arrow = TRUE,
        start_from = "bottomleft", first_seg = "horizontal",
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


LBS_search_area <- (scale^2) * (2 * range + 1)

euclid_search_area <- pi * (max_euclidean_distance ^ 2)

LBS_to_euclid_area_percentage <- 100 * (LBS_search_area / euclid_search_area)

LBS_search_area
cat(LBS_search_area, "\n")
cat(euclid_search_area, "\n")
cat(LBS_to_euclid_area_percentage, "\n")

