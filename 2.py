import pandas as pd
from sklearn.neural_network import MLPClassifier

data = pd.read_csv("backprop.csv")
X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values

model = MLPClassifier(
    hidden_layer_sizes = (4,),
    max_iter = 10000
)

model.fit(X,Y)

print(model.predict(X))