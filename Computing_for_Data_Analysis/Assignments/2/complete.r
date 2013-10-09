# Computing for Data Analysis
# Programming Assignment 2
# Andreas Zilly - October 2013
# 
# Part 2 - complete

# Working Directory:
setwd("~/coursera/Computing_for_Data_Analysis/Assignments/2")

complete <- function(directory, id = 1:332) {
    data <- data.frame(id=rep(0, length(id)), nobs=rep(0, length(id)), stringsAsFactors=FALSE)
    
    position = 1
    for(n_id in id) {
        id_name <- paste(c(getwd(), "/", directory, "/", formatC(as.integer(n_id), width = 3, flag = '0'), ".csv"),
                     sep="", collapse="")
        current_data <- read.table(id_name, , header=T, sep=",")
        data[position,] <- c(n_id, sum(!is.na(current_data$sulfate) & !is.na(current_data$nitrate)))
        
        position <- position + 1
    }
	
    data  # return values
}