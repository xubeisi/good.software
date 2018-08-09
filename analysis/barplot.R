#barplots in R 
library("ggplot2")
data=read.table("~/Software_Crisis/intervention.time.1",head=TRUE)
p <-ggplot(DF1, aes(x = pseudo, y =Intervention_percentage,fill=intervention)) + geom_bar(stat = "identity")
p + scale_x_discrete(limits=c("5X","15X","30X","60X","120X","140X"), labels=c("5","15","30","60","120","120(unsuccessfull)"))+scale_fill_manual(values=c("#66FF00", "#FF3300"))+xlab("installation time(mins)")

