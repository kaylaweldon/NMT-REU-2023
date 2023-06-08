library(HilbertCurve)
library(IRanges)

x <- sort(sample(1000, 20))
s <- x[1:10*2 - 1]
e <- x[1:10*2]
ir2 <- IRanges(s, e)

labels <- sample(letters, length(ir2), replace = TRUE)

hc <- HilbertCurve(1, 1023, level = 4)

# This is an other way to add background line
hc_segments(hc, IRanges(1, 1023))
hc_rect(hc, ir2, gp = gpar(fill = rand_color(length(ir2), transparency = 0.8)))
hc_polygon(hc, ir2[c(1, 3, 5)], gp = gpar(col = "red"))

# By setting np = 2 (for whatever order), 
# we simulate the actual grid under the curve
hc_points(hc, ir2, np = 2, gp = gpar(fill = rand_color(length(ir2))),
         shape = sample(c("square"), 
             length(ir2), size = 100, replace = TRUE))
hc_text(hc, ir2, labels = labels, 
    gp = gpar(fontsize = 40, col = "blue", font = 2))