library(HilbertCurve)
library(IRanges)

ir <- IRanges(start=c(0,256, 256 * 2, 256 * 3),
         end = c(255, 256 * 2 - 1, 256 * 3 - 1, 256 * 4 - 1))

hc1 <- HilbertCurve(0, 1023, level = 5, reference = TRUE)
hc_polygon(hc1, ir)
hc_text(hc1, ir, labels = c("III", "II", "I", "IV"),
            gp = gpar(font = 2, fontsize = 40))
