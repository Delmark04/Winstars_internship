----test3_docker----

Current directory consists of 4 files:

1. Dockerfile - file, that contains docker settings to the project;
2. internship_hidden_test.csv - file with input data to the prediction model;
3. model.py - model, that predicts target to dataset "internship_hidden_test.csv"
4. predict.csv - file, that contains target predicted by model

To run this docker project, we need to open command line, go to the directory with this project and execute next comands:

docker build . --tag predict

docker run -v ./your/dir:/pred predict

If you want to predict custom dataset, you need to set its name as an argument, for example:

docker run -v D:\Winstars\test3_docker:/pred predict internship_train.csv
