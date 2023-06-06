library(HilbertCurve)
library(circlize)
library(IRanges)

ir <- IRanges(start=c(90,15,60), end=c(100,30,70))

hc1 = HilbertCurve(1, 100, level = 5, reference = TRUE)
hc_rect(hc1, ir, gp = gpar(fill = "#FF000080"))
hc_points(hc1, ir)
hc_text(hc1, ir, labels = c("Ua", "Ub", "Uc"), gp = gpar(fontsize = width(ir)*2))

