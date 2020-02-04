import sys
from pydriller import RepositoryMining, GitRepository
import datetime
from splclassifier import SPLClassifier
#from manualcommits import getManualResultsKconfig, getMakeFileResultsManual, getAMFileResultsManual
from features import getLinuxF
from getCommitsLinux import getLinuxCommits
import re

dt1 = datetime.datetime(2017, 3, 8, 0, 0, 0)
dt2 = datetime.datetime(2017, 12, 31, 0, 0, 0)

repositorio = ''

GR = GitRepository('../soletta')

# KCONFIG EXAMPLES
# d458061abec39e7a0693c49f96b7ab3378c157d9 - only Removeds
# 2c727429e244c074a45c0d99b8ba57ad7fb6df36 - both (add at final)
# da5f77ff470f49e90797db27a8923c988c099e96 - replace inside file
# 9110b309393ec27dee35baf23d1cbefe1a796d8f -

# MAKEFILE EXAMPLES
# 17022a2622ddce9fbbd478a551f46e639d991cb0
# e6e17e41bbeb92125541c9cc4c06273ef1566c22
# ec6c506d1e926efa1007e9b5946d57a5e3f3804a
# 3e677dd8f3c6427a861a36f139f49c814f5dad88 FUDEU!!!!!! (REVER)
# 0c45273fb09534946b704fea99f64c7acbb14eea

fileKind = sys.argv[1]


# listaCommitsKconfigGeneral = getKconfigFiles()
# listaCommitsMakefileGeneral = getMakefileFiles()
# listaCommitsAMGeneral = getAMFiles()
listaCommitsLinux = getLinuxCommits()
features = []
if(fileKind == 'makefile'):
    print("SOU MAKEFILE")
    #listaCommitsLinux = getLinuxCommits()
    listaCommits = listaCommitsLinux
    features = getLinuxF()
    #arq = open('automated-results-makefile-linux.csv','w')
    arq = open('automated-rc-linux.csv','w')
        
elif(fileKind == 'kconfig'):
    print("SOU KCONFIG")
    #listaCommits = listaCommitsKconfig
    #arq = open('automated-results-kconfig-linux.csv','w')
    arq = open('automated-results-kconfig-uclibc.csv','w')
else:
    print("SOU AM")
    #listaCommits = listaCommitsAM
    arq = open('automated-results-am-linux.csv','w')

listaCommitResults = ['Hash,author,KC-Tags,MF-Tags,AM-Tags\n']
#features = getSPLFeatures()
features = getLinuxF()

pathLinux = '../../../journal/repositories/linux'
pathAxtls = '../../journal/repositories/axtls'
pathUclibc = '../../journal/repositories/uClibc'
githubLinux = 'https://github.com/torvalds/linux.git'

#for commit in RepositoryMining(pathLinux,only_commits=listaCommits).traverse_commits():

for commit in RepositoryMining(pathLinux,only_commits=listaCommits).traverse_commits():
#for commit in RepositoryMining(pathLinux,single='42e705e91f98637a6891eaf8a5c8dcce477b6378').traverse_commits():
#for commit in RepositoryMining(pathUclibc).traverse_commits():
    #print(commit.hash)
    #listaC = listaCommitsLinux
    
    kconfig_commit_tags = []
    makefile_commit_tags = []
    am_commit_tags = []
    commitResults = []
    # if(commit.hash in listaC):
    #     print('funfouuuu')

    for modification in commit.modifications:
        print('entrou nas modss')

        files_changing_tags = []
        if(('kconfig' in modification.filename.lower() or 'makefile' in modification.filename.lower()) and modification.change_type.value == 5):
            print('sou kconfig')
            diff = modification.diff
            parsed_lines = GR.parse_diff(diff)
            added = parsed_lines['added']
            removed = parsed_lines['deleted']
            file_source_code = modification.source_code.split('\n')
            classifier = SPLClassifier(added, removed, file_source_code)
            files_changing_tags = classifier.classify(modification.filename.lower(),features)
        # elif((re.match(r'\S*\.c', modification.filename.lower()) != None) or re.match(r'\S*\.h', modification.filename.lower()) != None):
        else:
            #print("SOU AM")
            if(modification.change_type.value != 1 and modification.change_type.value != 4):
                diff = modification.diff
                parsed_lines = GR.parse_diff(diff)
                added = parsed_lines['added']
                removed = parsed_lines['deleted']
                file_source_code = modification.source_code.split('\n')
                classifier = SPLClassifier(added, removed, file_source_code)
                files_changing_tags = classifier.classify(modification.filename.lower(),features)
                files_changing_tags.append('changeAsset')
            else:
                if(modification.change_type.value == 1):
                    files_changing_tags.append('addAsset')
                elif(modification.change_type.value == 4):
                    files_changing_tags.append('removeAsset')
        for file_tag in files_changing_tags:
            if('kconfig' in modification.filename.lower() and (file_tag not in kconfig_commit_tags)):
                kconfig_commit_tags.append(file_tag)
            elif('makefile' in modification.filename.lower() and (file_tag not in makefile_commit_tags)):
                makefile_commit_tags.append(file_tag)
            elif('kconfig' not in modification.filename.lower() and 'makefile' not in modification.filename.lower() and file_tag not in am_commit_tags):
                am_commit_tags.append(file_tag)
    if(len(kconfig_commit_tags) > 0):
        kconfig_commit_tags = str(kconfig_commit_tags).replace(',',' |')
    else:
        kconfig_commit_tags = 'no-tag-changed'
    if(len(makefile_commit_tags) > 0):
        makefile_commit_tags = str(makefile_commit_tags).replace(',',' |')
    else:
        makefile_commit_tags = 'no-tag-changed'
    if(len(am_commit_tags) > 0):
        am_commit_tags = str(am_commit_tags).replace(',',' |')
    else:
        am_commit_tags = 'no-tag-changed'
    mountStr = '{},{},{},{},{}\n'.format(commit.hash, commit.author.name, kconfig_commit_tags, makefile_commit_tags, am_commit_tags)
    listaCommitResults.append(mountStr)

#arqOut = open('output-linux.csv','w')
arq.writelines(listaCommitResults)
    


# Commit adhfaslkdgsakjdf:
#     arquivo X (mod): ("Remove", "Depends"), ("Added", "Feature")
#     arquivo Y (mod): ("Modify", "menu"), ("Remove", "Depends")

# Commit adhfaslkdgsakjdf: [("Remove", "Depends"), ("Added", "Feature"), ("Modify", "menu")]

# Teste
# menu "Bindings"	
# config USE_NODEJS	
# 	bool "Node.js bindings"	
# 	depends on HAVE_NODEJS && HAVE_NODEJS_NPM && HAVE_NODE_GYP
# 	default n
# 	help	
# 		Enable Node.js bindings
# endmenu

# if(condition1 && condition2)

# if(condiiton1){
#     if(condition2)
# }




# obj-$(PRINTER) += printers.mod


# obj-$(PARSERS) += parsers.mod
# obj-$(PARSERS) += $(LALALA)



# ifdef ($(IDK),)
# -include LALALA.gen
# endif


# ifneq ($(HAVE_KCONFIG_CONFIG),)
# -include Makefile.gen
# endif







