import pandas as pd

data = pd.read_csv("finds.csv")

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

h = ['0'] * len(X[0])

for i in range(len(Y)):
    if Y[i] == 'Yes':
        for j in range(len(h)):
            if h[j] == '0':
                h[j] = X[i][j]
            elif h[j] != X[i][j]:
                h[j] = '?'

print("Final Hypothesis:", h)
