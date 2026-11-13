import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv("knn.csv")
X = data.iloc[:,: -1]
Y = data.iloc[:,-1]

model = KNeighborsClassifier(n_neighbors = 2)
model.fit(X,Y)

print(model.predict(X))
print(model.predict([[30,35000]]))
