library(HilbertCurve)
library(IRanges)
library(circlize)
library(HilbertVis)

# x = sort(sample(100, 20))
# s = x[1:10*2 - 1]
# e = x[1:10*2]
# ir = IRanges(150, 175)
# ir

# hc = HilbertCurve(1, 16, level = 2, reference = TRUE, title = "np = 3")
# hc_points(hc, x1 = 1, x2 = 2, np = 3)


# hc = HilbertCurve(1, 500, level = 5, reference = TRUE)
# hc_points(hc, ir)

# for(i in 1:1024) {
#     hc = HilbertCurve(1, 1024, level = 5, reference = TRUE, arrow = TRUE)
#     hc_points(hc, x1 = i, np = NULL, pch = 16, size = unit(2, "mm"))
# }

pos = HilbertVis::hilbertCurve(8)
mat = as.matrix(dist(pos))
library(ComplexHeatmap)

ht = Heatmap(mat, name = "dist", cluster_rows = FALSE, cluster_columns = FALSE, 
    show_row_names = FALSE, show_column_names = FALSE, 
    heatmap_legend_param = list(title = "euclidean_dist"))
draw(ht, padding = unit(c(5, 5, 5, 2), "mm"))
decorate_heatmap_body("dist", {
    grid.segments(c(0.25, 0.5, 0.75, 0, 0, 0), c(0, 0, 0, 0.25, 0.5, 0.75), 
          c(0.25, 0.5, 0.75, 1, 1, 1), c(1, 1, 1, 0.25, 0.5, 0.75), gp = gpar(lty = 2))
    grid.text(rev(c(256, 512, 768, 1024)), 0, c(0, 256, 512, 768)/1024, just = "bottom", 
        rot = 90, gp = gpar(fontsize = 10))
    grid.text(c(1, 256, 512, 768, 1024), c(1, 256, 512, 768, 1024)/1024, 1, just = "bottom",
        gp = gpar(fontsize = 10))
})
