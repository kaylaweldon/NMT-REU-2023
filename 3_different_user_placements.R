library(HilbertCurve)
library(circlize)
library(IRanges)

ir <- IRanges(start = c(0, 38, 90, 155, 230), end = c(10, 48, 100, 165, 240))

hc1 <- HilbertCurve(0, 255, level = 4, arrow = TRUE,
        reference = TRUE, padding = unit(6, "cm"))

hc_rect(hc1, ir, gp = gpar(fill = rand_color(length(ir), transparency = 0.6)))

hc_points(hc1, x1 = c(5, 43, 95, 160, 235), x2 = c(5, 43, 95, 160, 235),
        np = 1, shape = "circle", size = unit(1.5 * 10, "cm"))

hc_text(hc1, ir, labels = c("a", "b", "c", "d", "e"),
        gp = gpar(fontsize = 33, col = "black", font = 2))
