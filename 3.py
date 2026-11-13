import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import OrdinalEncoder
import matplotlib.pyplot as plt

data = pd.read_csv("id3.csv")
X = data.iloc[:,:-1].values
Y = data.iloc[:,-1].values

encoder = OrdinalEncoder()
X = encoder.fit_transform(X)

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X,Y)

print(model.predict(X))
plot_tree(model, filled = True)
plt.show()
