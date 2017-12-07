###############################################################
#                                                             #
#            Test the New dataset using saved Model           #
#                                                             #
###############################################################
#                                                             #
# Credit: Dr. Prashant Singh Rana                             #
# Email : psrana@gmail.com                                    #
# Web   : www.psrana.com                                      #
#                                                             #
###############################################################
#                                                             #
# This script do the following:                               #
# 1. Load the Model                                           #
# 2. Test the new Dataset                                     #
# 3. Finally Saving the results.                              #
#                                                             #
###############################################################



#--------------------------------------------------------------
# Step 1: Include Library
#--------------------------------------------------------------
library(randomForest)


#--------------------------------------------------------------
# Step 2: Variable Declaration
#--------------------------------------------------------------
cat("\nStep 2: Variable Declaration")
modelFileName <- "randomForest-Model.RData"
testFileName  <-"regressionDataSet.csv"



#--------------------------------------------------------------
# Step 3: Model Loading
#--------------------------------------------------------------
cat("\nStep 3: Model Loading")
load(modelFileName)



#--------------------------------------------------------------
# Step 4: Data Loading
#--------------------------------------------------------------
cat("\nStep 4: Data Loading")
newTestDataset <- read.csv(testFileName)    # Read the datafile
head(newTestDataset)


#--------------------------------------------------------------
# Step 5: Prediction (Testing)
#--------------------------------------------------------------
cat("\nStep 5: Prediction using -> ", modelName)
NewPredicted <- predict(model, newTestDataset)
head(NewPredicted)


#--------------------------------------------------------------
# Step 6: Saving Results
#--------------------------------------------------------------
cat("\nStep 6: Saving Results")
write.csv(data.frame(newTestDataset,NewPredicted), file=paste(modelName,"-Testing-Result.csv",sep=''), row.names=FALSE)


cat("\nDone")

#--------------------------------------------------------------
#                           END 
#--------------------------------------------------------------

