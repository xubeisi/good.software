#!/usr/bin/env Rscript
library(ggplot2)

data=read.csv("abstractLinks.csv")
pdf("Number.links.by.journal.year.pdf",width=10,height=4)
qplot(data$year, colour=factor(journal), data=data, geom="density")
dev.off()

