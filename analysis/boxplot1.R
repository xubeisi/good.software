#boxplots with transparent graphs and colored points
library("ggplot2")
p2 = ggplot(data, aes(x=source, y=time)) +geom_point(aes(fill=source), size=4, shape=21, colour="grey20",position=position_jitter(width=0.2, height=0.1)) +geom_boxplot(outlier.colour=NA, fill=NA, colour="black") 
p2+ theme_bw() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()) # remove background
#p2+ scale_x_discrete(limits=c("Easy_install","Complex_install","Not_installed")) : rename the x axis 

