import pandas as pd
import numpy as np
import sys

def model(data):
    test = pd.read_csv(data)
    pred_transpose = np.array(test['6']**2+test['7'])
    return np.savetxt("predict.csv", pred_transpose, delimiter=",")
# path = "./predict/"
name = sys.argv[1]#"internship_hidden_test.csv"
model(name)
print(f"{name}, was predicted to predict.csv!")