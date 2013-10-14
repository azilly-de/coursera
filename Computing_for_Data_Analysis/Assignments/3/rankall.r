# Computing for Data Analysis
# Programming Assignment 3
# Andreas Zilly - October 2013
# 
# Part 6 - Ranking hospitals in all states
#
# Working Directory:
setwd("~/coursera/Computing_for_Data_Analysis/Assignments/3")

rankall <- function(outcome, num="best") {
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
  data <- data[c(2, 7, columns[[outcome]])]
  suppressWarnings(data[,3] <- as.numeric(data[,3]))
  
  state_names <- unique(data$State)
  state_names <- state_names[order(state_names)]
  
  data_frame <-  data.frame(hospital=rep(NA, length(state_names)),
                            state=rep(NA, length(state_names)),
                            stringsAsFactors=FALSE)

  counter <- 1
  for(state in state_names) {
    state_data <- data[data$State == state,]
    state_data <- state_data[order(state_data[,3], state_data[,1]), ]
    
    suppressWarnings(
      show_rank <- as.numeric(num) 
    )
    
    if(!is.na(show_rank)) {
      value <- c(state_data[show_rank,1], state)
    } else if(num == "worst") {
      value <- c(state_data[length(state_data[,1]),1], state)
    } else if(num == "best"){
      value <- c(state_data[1,1], state)
    } else {
      value <- c(NA, state)
    }
    
    data_frame[counter,] <- value
    counter <- counter + 1
  }

  # Return values
  data_frame
}
