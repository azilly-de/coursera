# Computing for Data Analysis
# Programming Assignment 2
# Andreas Zilly - October 2013
# 
# Part 1 - getmonitor

# Working Directory:
setwd("~/coursera/Computing_for_Data_Analysis/Assignments/2")

getmonitor <- function(id, directory, summarize = FALSE) {
    id_name <- paste(c(getwd(), "/", directory, "/", formatC(as.integer(id), width = 3, flag = '0'), ".csv"),
                  sep="", collapse="")
    data <- read.table(id_name, , header=T, sep=",")
    
    if(summarize == TRUE) {
      print(summary(data))
    }
    
    data # return values
}