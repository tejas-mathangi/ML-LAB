import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("kmeans.csv")
X = data.values

model = KMeans(n_clusters=3)
model.fit(X)

print("Cluster Labels:", model.labels_)
print("Cluster Centers:", model.cluster_centers_)