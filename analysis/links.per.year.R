#!/usr/bin/env Rscript

library(ggplot2)

data=read.csv("results.links.type.per.year.csv")
pdf("results.links.type.per.year.pdf",width=10,height=4)

ggplot(data=data, aes(x=year, y=prc*100,fill=status)) + geom_bar(stat="identity") + theme_classic() + scale_fill_manual(values=c("red", "dark red", "#66CC99", "dark green"))

dev.off()

