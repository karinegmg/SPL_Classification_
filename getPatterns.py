fileName = 'saida_rc_corretos.csv'

def getPatterns(queryList):
    file_tags = open(fileName, 'r')
    count = 0
    dictTags = {}
    result = 'result = '
    for commit in file_tags:
        lines = commit.split(',')
        hashCommit = lines[0][0:10]
        tags = lines[2] + lines[3] + lines[4]
        dictTags[hashCommit] = tags

    for key, v in dictTags.items():
        aux = 0
        for q in queryList:
            if(q in v):
                aux = aux + 1
            if(aux == len(queryList)):
                count = count + 1
                #print('match: ', v)
    
    result = result + str(count)
        
    return result

'''
Change Type = Added, Modify, Remove, New
Tags FM = ('Added' | 'Feature'), ('Added' | 'Depends'), ('Added' | 'Default'), ('Added' | 'Select')
Tags CK = ('Modify' | 'Mapping'), ('Modify' | 'ifdef'), ('Modify' | 'build')]
Tags AM = 'changeAsset', 'addAsset', 'removeAsset'
'''
# Query Example: How often commits present changes which add feature in Kconfig and a mapping in Makefile?
queryList = ["('Added' | 'Feature')", "('Modify' | 'Mapping')"]
query = getPatterns(queryList)

print(query)