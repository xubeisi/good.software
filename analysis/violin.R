#makes a violin plot in R
library("ggplot2")
data=read.table("~/abc/xyz",head=TRUE)
p2 <- ggplot(data, aes(x =example, y = citations,fill=example))+geom_violin()
