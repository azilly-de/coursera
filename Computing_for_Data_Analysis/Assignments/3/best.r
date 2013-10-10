# Computing for Data Analysis
# Programming Assignment 3
# Andreas Zilly - October 2013
# 
# Part 5 - Finding best hospital in state
#
# ! no handling of ties !
#
# Working Directory:
setwd("~/coursera/Computing_for_Data_Analysis/Assignments/3")

best <- function(state, outcome) {
    # Read outcome data      
    data <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
  
    columns <- list()
    columns[["heart attack"]] <- 11
    columns[["heart failure"]] <- 17
    columns[["pneumonia"]] <- 23
    
    # Validate outcome
    if(is.null(columns[[outcome]])) {
      stop("invalid outcome")
    }
    
    # Manipulate data
    data <- data[data$State == state,]
    
    # Validate state
    if( length(data[,2]) == 0) {
      stop("invalid state")
    }
  
    data <- data[c(2, columns[[outcome]])]
    suppressWarnings(data[,2] <- as.numeric(data[,2]))
    value <- which(data[2] == min(data[2], na.rm=T))
    
    hospital <- data[value,]$Hospital.Name
    # ! no handling of ties !
  
    hospital  
}