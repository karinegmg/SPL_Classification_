import pandas as pd
from sklearn.cluster import KMeans, OPTICS
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.manifold import TSNE
from scipy.cluster.hierarchy import dendrogram, linkage

fileName = 'automatic_classification_output/rc_linux_classification_with_date.csv'
output = 'linux_data_get_dummies_teste.csv'
outputFile = open(output, 'w')

fileD = 'linux_dataset.csv'
fileDummies = open(fileD, 'w')

commits = open(fileName, 'r')
newLine = '{},{},{}\n'.format('hash', 'date', 'tags')
outputFile.write(newLine)

def get_dummies_format():

    for c in commits:
        line = c.split(',')
        hashCommit = line[0]
        dateCommit = line[1]
        allTags = ''

        tagsFM = (line[2].replace('[(', '').replace(')]', '')).split(') | (')
        tagsCK = (line[3].replace('[(', '').replace(')]', '')).split(') | (')
        tagsAM = (line[4].replace('[', '').replace(']', '')).split(' | ')

        print(tagsCK)
        #print(tagsCK, tagsFM)
        #allTags = "{}/{}/{}".format(tagsFM.replace(',',"/"), tagsCK.replace(',',"/"), tagsAM.replace(',',"/"))

        if ('september' in dateCommit):
            dateCommit = '9'
        if ('october' in dateCommit):
            dateCommit = '10'
        if ('november' in dateCommit):
            dateCommit = '11'
        if ('december' in dateCommit):
            dateCommit = '12'
        if ('january' in dateCommit):
            dateCommit = '1'
        
        for fm in tagsFM:
            fm = fm.replace("(","").replace(")","").replace(' | ', '').replace("|","").replace("'",'')
            allTags = '{}|{}'.format(allTags, fm)
        for ck in tagsCK:
            ck = ck.replace("(","").replace(")","").replace(' | ', '').replace("|","").replace("'",'')
            allTags = '{}|{}'.format(allTags, ck)
        for am in tagsAM:
            allTags = '{}|{}'.format(allTags, am.replace("'",''))
        

        newLine = '{},{},{}'.format(hashCommit, dateCommit, allTags[1:])
        outputFile.write(newLine)
        
get_dummies_format()
outputFile.close()

output = 'linux_data_get_dummies_teste.csv'

saida_dos_grupos = 'saida_teste.csv'
saida_file = open(saida_dos_grupos, 'w')

dataset = pd.read_csv(output, delimiter=',')
#output_dataset = pd.get_dummies(dataset, columns =['tags'])
tags_output = dataset.tags.str.get_dummies()

print(tags_output[tags_output.sum(axis=1)==26].iloc[0])


#print(tags_output.sum(axis=1))
dummy = pd.concat([dataset, tags_output], axis=1)
#print(dummy.head())
#print(dummy.columns)
X = dummy.iloc[:, :].values

scaler = StandardScaler()
tags_scaler = scaler.fit_transform(tags_output)
#print(tags_scaler)

#print(tags_output.columns)
model = KMeans(n_clusters = 12)
model.fit(tags_scaler)

'groups {}'.format(model.labels_)
model.cluster_centers_


groups = pd.DataFrame(model.cluster_centers_, columns = tags_output.columns)
groups

# groups.transpose().plot.bar(subplots=True,
#                figsize=(25, 50),
#                sharex=False,
#                rot=0)


linha = 'grupo, commits'
saida_file.write(linha)

matriz_de_distancia = linkage(groups)
matriz_de_distancia
dendrograma = dendrogram(matriz_de_distancia)
sum = 0
for i in range(12):
   grupo = i
   filtro = model.labels_ == grupo
   print('grupo: {} e qtd: {}'.format(i, len(dummy[filtro])))
   sum = sum + len(dummy[filtro])
  #  df = dummy[filtro]
  #  print(df[3:])
   linha = '{}, {}'.format(i, dummy[filtro].hash)
   saida_file.write(linha)
print(sum)

saida_file.close()
# grupo = 8
# filtro = model.labels_ == grupo
# print(len(dummy[filtro]))


tsne = TSNE()
visualizacao = tsne.fit_transform(tags_scaler)
print(visualizacao)

# sns.set(rc={'figure.figsize': (13, 13)})
# sns.scatterplot(x=visualizacao[:, 0],
#                y=visualizacao[:, 1],
#                hue=model.labels_,
#                palette='viridis')

#sns.set(rc={'figure.figsize': (13, 13)})


####################### tentando encontrar o "cotovelo" da amostra
# def kmeans(num_clusters, tags):
#   model = KMeans(n_clusters=num_clusters)
#   model.fit(tags)
#   return [num_clusters, model.inertia_]

# result = [kmeans(n_groups, tags_scaler) for n_groups in range(1, 35)]
# result

# result = pd.DataFrame(result, 
#            columns=['grupos', 'inertia'])
# #result: acho que deu 11 ou 12
# result.inertia.plot()
################################################

# groups.transpose().plot.bar(subplots=True,
#                figsize=(25, 50),
#                sharex=False,
#                rot=0)