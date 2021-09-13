'''
Change Type = Added, Modify, Remove, New
Tags FM = ('Added' | 'Feature'), ('Added' | 'Depends'), ('Added' | 'Default'), ('Added' | 'Select')
Tags CK = ('Modify' | 'Mapping'), ('Modify' | 'ifdef'), ('Modify' | 'build')]
Tags AM = 'changeAsset', 'addAsset', 'removeAsset'
No tags in each space = no-fm-tag-changed or no-ck-tag-changed or no-am-tag-changed
'''

fileName = 'automatic_classification_output/rc_linux_classification_with_date.csv'
output = 'linux_data_numbers_comma_test.csv'
outputFile = open(output, 'w')

commits = open(fileName, 'r')

tagsList = ["('Added' | 'Feature')", "('Added' | 'Depends')", "('Added' | 'Menu')", "('Added' | 'Default')", 
"('Added' | 'Select')", "('Added' | 'build')", "('Added' | 'Mapping')", "('Added' | 'ifdef')", "('Modify' | 'Select')",
"('Modify' | 'Feature')", "('Modify' | 'Depends')", "('Modify' | 'Menu')", "('Modify' | 'Default')", "('Modify' | 'build')", "('Modify' | 'Mapping')",
"('Modify' | 'ifdef')", "('Remove' | 'Select')", "('Remove' | 'Feature')", "('Remove' | 'Depends')", "('Remove' | 'Menu')",
"('Remove' | 'Default')", "('Remove' | 'build')", "('Remove' | 'Mapping')", "('Remove' | 'ifdef')", "('New' | 'Select')",
"('New' | 'Feature')", "('New' | 'Depends')", "('New' | 'Menu')", "('New' | 'Default')", "('New' | 'build')",
"('New' | 'Mapping')", "('New' | 'ifdef')"]

for c in commits:    
    line = c
    interator = 1
    #allTags = line.split(',')

    for tags in tagsList:
        line = line.replace(tags, str(interator))
        interator = interator + 1
        line = line.replace("'changeAsset'", '100')
        line = line.replace("'addAsset'", '200')
        line = line.replace("'removeAsset'", '300')
        line = line.replace("no-fm-tag-changed", '700')
        line = line.replace("no-ck-tag-changed", '800')
        line = line.replace("no-am-tag-changed", '900')
        #or replace for comma 
    line = line.replace("[", '')
    line = line.replace("]", '')
    line = line.replace("|", ',')
    outputFile.write(line)
   

outputFile.close()

    