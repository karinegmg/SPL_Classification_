import seaborn as sns
import pandas as pd
import numpy as np #para manipular os vetores
from matplotlib import pyplot as plt #para plotar os gráficos
from sklearn.cluster import KMeans #para usar o KMeans

plt.style.use('seaborn')

fileName = 'linux_data_numbers_comma.csv'
# linux = pd.read_csv(fileName)
linux = pd.read_csv(fileName, delimiter=',')
linux.head()
X = linux.iloc[:, 1:4].values

kmeans = KMeans(n_clusters = 3, init = 'random')
print(kmeans.fit(X))

# plt.scatter(linux[:, 0], linux[:,1], s = 100, c = kmeans.labels_)
# plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'red',label = 'Centroids')
# plt.title('Iris Clusters and Centroids')
# plt.xlabel('SepalLength')
# plt.ylabel('SepalWidth')
# plt.legend()

# plt.show()


#kmeans.predict(data)

