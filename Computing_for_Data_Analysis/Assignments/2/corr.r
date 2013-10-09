# Computing for Data Analysis
# Programming Assignment 2
# Andreas Zilly - October 2013
# 
# Part 3 - corr
source('~/coursera/Computing_for_Data_Analysis/Assignments/2/getmonitor.r')
source('~/coursera/Computing_for_Data_Analysis/Assignments/2/complete.r')

# Working Directory:
setwd("~/coursera/Computing_for_Data_Analysis/Assignments/2")

corr <- function(directory, threshold = 0) {
    nobs_data <- complete(directory)
    nobs_data <- nobs_data[nobs_data$nobs >= threshold, ]
    
    data <- data.frame(corr=rep(0, length(nobs_data$id)), stringsAsFactors=FALSE)
    position = 1
    
    for(id in nobs_data$id) {
      current <- getmonitor(id, directory)
      current_corr <- cor(current$sulfate, current$nitrate, use="pairwise.complete.obs")
      
      data[position,] <- current_corr
      
      position <- position + 1
    }

    data$corr #Return values
}