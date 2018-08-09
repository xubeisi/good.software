#boxplot with colored bars and black points
library("ggplot2")
data=read.table("~/Software_Crisis/source.time",head=TRUE)
qplot( x=source , y=time , data=data , geom=c("boxplot","jitter"),fill=source)	

