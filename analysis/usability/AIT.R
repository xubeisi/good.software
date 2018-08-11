library(ggplot2)

data=read.csv('table.SC.csv')

pdf('AIT.pdf',width=6,height=6)
ggplot(data, aes(x=AIT, y= time, fill=AIT))+ geom_violin()+theme(axis.text.x = element_text(angle=90)) +theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank(),panel.background = element_blank(), axis.line = element_line(colour = "black"))+theme(legend.position="none")+labs(y = "Time (min)")+labs(x = "Automatic Instalation Test")+theme(axis.text=element_text(size=20),axis.title=element_text(size=15,face="bold"))+scale_y_continuous(breaks = seq(0, 120, by = 20))

dev.off()
