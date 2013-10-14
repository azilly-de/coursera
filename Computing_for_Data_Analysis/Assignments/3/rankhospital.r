# Computing for Data Analysis
# Programming Assignment 3
# Andreas Zilly - October 2013
# 
# Part 6 - Ranking hospitals by outcome in a state
#
# Working Directory:
setwd("~/coursera/Computing_for_Data_Analysis/Assignments/3")

rankhospital <- function(state, outcome, num = "best") {
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
    data <- data[order(data[,2], data[,1]), ]
    data <- data[complete.cases(data),]
    
    # Rename column
    names(data)[2] <- "Rate"
    
    # Add Rank column
    data$Rank <- seq(1, length(data$Rate))  
    suppressWarnings(
      show_rank <- as.numeric(num) 
      )
    
    # Return value
    if(!is.na(show_rank)) {
      data[show_rank,1]
    } else if(num == "worst") {
      data[length(data$Rank),1]
    } else {
      data[0,1]
    }
}