import random

randomList = []

while (len(randomList) < 30):
    num = random.randint(1, 500)
    if (num not in randomList):
        randomList.append(num)
    
fileName = 'saida_rc_corretos.csv'
automaticResultsFile = open(fileName, 'r')
listCommits = []

for commit in automaticResultsFile:
    listCommits.append(commit)


outputFile = 'random_commits.csv'
randomCommits = open(outputFile, 'w')

randomCommits.write('Hash,author,KC-Tags,MF-Tags,AM-Tags\n')

for item in randomList:
    randomCommits.write(listCommits[item])

randomCommits.close()