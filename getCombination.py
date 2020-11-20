fileName = 'linux_data_get_dummies_teste.csv'
fileIn = open(fileName, 'r')
tagsDiff = []
dictCommits = {}
dictTagsAndAmount = {}
countPattern = 0 

fileOutName = 'tags_patterns.csv'
fileOut = open(fileOutName, 'w')

#fileOut.write('amount, tags\n')

for fi in fileIn:
    line = fi.strip().split(',')
    tags = line[2].split('|')
    # print(tags)
    sortedTags = str(sorted(tags))
    print(sortedTags)

    if(not sortedTags in dictTagsAndAmount):
        dictCommits[(tags[0])[0:10]] = sortedTags
        dictTagsAndAmount[sortedTags] = '0'
    
    if(sortedTags in dictTagsAndAmount):
        countTag = dictTagsAndAmount[sortedTags]
        dictTagsAndAmount[sortedTags] = str(int(countTag) + 1)
        
for i in dictTagsAndAmount:
    fileOut.write('{}, Tags = {}\n'.format(dictTagsAndAmount[i], i.replace(',', "|")))

fileOut.close()
# print(dictTagsAndAmount)

