----test3_docker----

Current directory consists of 4 files:

Dockerfile - file, that contains docker settings to the project;
internship_hidden_test.csv - file with input date to the prediction model;
model.py - model, that predicts target to dataset "internship_hidden_test.csv"
predict.csv - file, that contains target predicted by model
To run this docker project, we need to open command line and execute next comands:

docker build . --tag predict

docker run -v ./your/dir:/pred predict

If you want to predict custom dataset, you need to set its name as an argument, for example:

docker run -v D:\Winstars\test3_docker:/pred predict internship_train.csv
