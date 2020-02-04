from pydriller import RepositoryMining, GitRepository
import datetime
import re

def getLinuxF():
    featuresL = []
    featLinux = open('featuresLinux.csv', 'r')
    #testeString = ''

    for f in featLinux:
        #print(f.strip())
        testeString = '{}{}'.format('CONFIG_',f.strip())
        print(testeString)
        featuresL.append(testeString)
    
    return featuresL

