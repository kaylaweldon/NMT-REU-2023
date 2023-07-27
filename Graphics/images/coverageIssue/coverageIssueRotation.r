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

# eyeballing equal placements in the grid for "a"

# placements of "a" for NORMAL HC
# rotate 0   degrees normal -> ("bottomleft", "horizontal" ) = 43
# rotate 90  degrees normal -> ("topleft", "vertical") = 214
# rotate 180 degrees normal -> ("topright", "horizontal") = 131
# rotate 270 degrees normal -> ("bottomright", "vertical") = 126

# placements of "a" for TRANSPOSED HC
# rotate 0   degrees transposed -> ("bottomleft", "vertical") = 41
# rotate 90  degrees transposed -> ("topleft", "horizontal") = 124
# rotate 180 degrees transposed -> ("topright", "vertical") = 129
# rotate 270 degrees transposed -> ("bottomright", "horizontal") = 212

# notice an interesting pattern in the above: each seem to be 
# the same placement as a transposed version but by a difference of 2 cells

locationA <- 41

# the side length, in cm, of one cell
# this is a constant, don't change.
scale <- 1.3

# the max disance from user in real space, represented by a circle
max_euclidean_distance <- 5

# adjust the range to be searched by the LBS.
# a factor of 1 means LBS searches 1 unit for every euclidean unit
adjustment_factor <- 7

# calculate range to be searched by LBS
# i.e. the number of cells to search ahead and behind the user
range <- floor(((max_euclidean_distance - (scale / 2)) / scale))  * adjustment_factor
x <- range


# seperate tables are made for the purposes of selecting different colors that are not random
irA <- IRanges(start = c(locationA - x), end = c(locationA + x))


# construction of the hilbert curve
hc1 <- HilbertCurve(0, 255, level = 4, arrow = TRUE,
        start_from = "bottomleft", first_seg = "vertical",
        reference = TRUE, padding = unit(6, "cm"))


# VISUALIZE LBS SEARCH AREA

# color the area searched
hc_rect(hc1, irA, gp = gpar(fill = "#e3adf184", transparency = 0.6))

# outline of each cell searched
# hc_points(hc1, irA, np = 2, shape = "square")

# uncomment the following snippet to add a grid to the entire graph
# hc_points(hc1, x1 = 0, x2 = 255, np = 2, shape = "square")


# VISUALIZE USER PLACEMENT
hc_text(hc1, x1 = locationA, x2 = locationA, 
        label = "a", gp = gpar(fontsize = 25, col = "black", font = 2))


# VISUALIZE EUCLIDEAN SEARCH AREA
hc_points(hc1,   x1 = locationA, 
                 x2 = locationA,
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