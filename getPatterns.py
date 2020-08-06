filename = 'saida_rc_corretos.csv'
file_tags = open(filename, 'r')


dict_fm = {}
dict_ck = {}
dict_am = {}
lines = []
queryExampleCK = "('Modify' | 'Mapping')"
queryExampleFM = "('Added' | 'Feature')"
count = 0

for commit in file_tags:
    lines = commit.split(',')
    hashCommit = lines[0][0:10]
    #print(hashCommit)
    tags_fm = lines[2]
    tags_ck = lines[3]
    tags_am = lines[4]
    
    dict_fm[hashCommit] = tags_fm
    dict_ck[hashCommit] = tags_ck
    dict_am[hashCommit] = tags_am

for key, v in dict_fm.items():
    if(queryExampleFM in v):
        if(queryExampleCK in dict_ck[key]):
            print(key, v, dict_ck[key])
            count = count + 1
        #print(v)
print(count)



