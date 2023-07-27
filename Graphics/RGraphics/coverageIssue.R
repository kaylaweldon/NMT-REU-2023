# CITATION OF LIBRARY USED: HILBERTCURVE
#   Gu, Z. (2016) HilbertCurve: an R/Bioconductor package for
#   high-resolution visualization of genomic data. Bioinformatics.

# Carmen Day (2023)
# this code conveys the difference between distance measured by LBS
# vs distance as measured in Euclidean space.
#
# the thing that is really tricky here with visuals is the scale.
# I eyeballed it. 
# by measuring a circle of 1.3 cm diameter to what appeared to be one cell.

library(HilbertCurve)
library(circlize)
library(IRanges)

# set cell positions for four users.
# code is designed for exactly four users.
locationA <- 43
locationB <- 95
locationC <- 160
locationD <- 235

# the side length, in cm, of one cell
# this is a constant, don't change.
scale <- 1.3

# the max disance from user in real space, represented by a circle
max_euclidean_distance <- 5

# adjust the range to be searched by the LBS.
# a factor of 1 means LBS searches 1 unit for every euclidean unit
adjustment_factor <- 1

# calculate range to be searched by LBS
# i.e. the number of cells to search ahead and behind the user
range <- floor(((max_euclidean_distance - (scale / 2)) / scale))  * adjustment_factor
x <- range


# seperate tables are made for the purposes of selecting different colors that are not random
irA <- IRanges(start = c(locationA - x), end = c(locationA + x))
irB <- IRanges(start = c(locationB - x), end = c(locationB + x))
irC <- IRanges(start = c(locationC - x), end = c(locationC + x))
irD <- IRanges(start = c(locationD - x), end = c(locationD + x))


# construction of the hilbert curve
hc1 <- HilbertCurve(0, 255, level = 4, arrow = TRUE,
        start_from = "bottomleft", first_seg = "horizontal",
        reference = TRUE, padding = unit(6, "cm"))


# VISUALIZE LBS SEARCH AREA

# color the area searched
hc_rect(hc1, irA, gp = gpar(fill = "#e3adf184", transparency = 0.6))
hc_rect(hc1, irB, gp = gpar(fill = "#93d9dd86", transparency = 0.6))
hc_rect(hc1, irC, gp = gpar(fill = "#eeeb9088", transparency = 0.6))
hc_rect(hc1, irD, gp = gpar(fill = "#ff80807b", transparency = 0.6))

# outline of each cell searched
# hc_points(hc1, irA, np = 2, shape = "square")
# hc_points(hc1, irB, np = 2, shape = "square")
# hc_points(hc1, irC, np = 2, shape = "square")
# hc_points(hc1, irD, np = 2, shape = "square")

# uncomment the following snippet to add a grid to the entire graph
# hc_points(hc1, x1 = 0, x2 = 255, np = 2, shape = "square")


# VISUALIZE USER PLACEMENT
hc_text(hc1, x1 = locationA, x2 = locationA, label = "a", gp = gpar(fontsize = 25, col = "black", font = 2))
hc_text(hc1, x1 = locationB, x2 = locationB, label = "b", gp = gpar(fontsize = 25, col = "black", font = 2))
hc_text(hc1, x1 = locationC, x2 = locationC, label = "c", gp = gpar(fontsize = 25, col = "black", font = 2))
hc_text(hc1, x1 = locationD, x2 = locationD, label = "d", gp = gpar(fontsize = 25, col = "black", font = 2))

# VISUALIZE EUCLIDEAN SEARCH AREA
hc_points(hc1, x1 = c(locationA, locationB, locationC, locationD), 
                x2 = c(locationA, locationB, locationC, locationD),
        np = 1, shape = "circle",
        size = unit(2 * max_euclidean_distance, "cm"))


# CALCULATIONS

# area of one cell times total cells searched, including user cell
LBS_search_area <- (scale^2) * (2 * range + 1)

# area of a circle of radius max distance
euclid_search_area <- pi * (max_euclidean_distance ^ 2)

# ratio of the two areas
LBS_to_euclid_area_percentage <- 100 * (LBS_search_area / euclid_search_area)


# PRINT STATEMENTS

print("SCALE: Side length of one cell in meters (for example): ")
print(scale) 

print("Max Euclidean distance in meters (for example): ")
print(max_euclidean_distance)

print("adjustment factor: ")
print(adjustment_factor)

print("Max LBS distance in cells: cell range in one direction not including user cell: ")
print(range)

# display areas
print("LBS SEARCH AREA:")
cat(LBS_search_area, "\n")
print("EUCLID SEARCH AREA: ")
cat(euclid_search_area, "\n")

# display ratio
print("PERCENTAGE COVERED BY LBS: ")
cat(LBS_to_euclid_area_percentage, "\n")



# TEST SCALE UNIT FOR VISUALS

# test the unit of one cell. This is how the scale 1.3 was obtained. 
# hc_points(hc1, x1 = 0, x2 = 4, np = 1, size = unit(1.3, "cm"), shape = "circle")
# hc_points(hc1, x1 = 0, x2 = 255, np = 2, shape = "square")

