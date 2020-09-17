import pandas as pd

fileName = 'automatic_classification_output/rc_linux_classification_with_date.csv'
output = 'linux_data_get_dummies.csv'
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
        tagsFM = (line[2].replace('[(', '').replace(')]', '').replace("'",'')).split(') | (')
        tagsCK = (line[3].replace('[(', '').replace(')]', '').replace("'",'')).split(') | (')
        tagsAM = (line[4].replace('[', '').replace(']', '').replace("'",'').strip()).split(' | ')
        print(tagsCK, tagsFM)
        
        for fm in tagsFM:
            newLine = '{},{},{}\n'.format(hashCommit, dateCommit, fm)
            outputFile.write(newLine)
        for ck in tagsCK:
            newLine = '{},{},{}\n'.format(hashCommit, dateCommit, ck)
            outputFile.write(newLine)
        for am in tagsAM:
            newLine = '{},{},{}\n'.format(hashCommit, dateCommit, am)
            outputFile.write(newLine)
        
get_dummies_format()
outputFile.close()

dataset = pd.read_csv(output, delimiter=',')
saida = pd.get_dummies(dataset['tags'])
#print(saida)




