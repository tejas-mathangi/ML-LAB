import pandas as pd
data = pd.read_csv("candidate.csv")

X = data.iloc[:, :-1].values
Y = data.iloc[:, -1].values

n = len(X[0])

S = ['0'] * n
G = [['?' for i in range(n)]]

for i in range(len(Y)):
    if Y[i] == 'Yes':
        for j in range(n):
            if S[j] == '0':
                S[j] = X[i][j]
            elif S[j] != X[i][j]:
                S[j] = '?'

        new_G = []
        for g in G:
            valid = True
            for j in range(n):
                if g[j] != '?' and g[j] != S[j]:
                    valid = False
            if valid:
                new_G.append(g)

        G = new_G

    else:
        new_G = []
        for g in G:
            for j in range(n):
                if g[j] == '?' and S[j] != '?':
                    temp = g.copy()
                    temp[j] = S[j]
                    new_G.append(temp)

        G = new_G

print("Specific Boundary:", S)
print("General Boundary:", G)