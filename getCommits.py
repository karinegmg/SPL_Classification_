from pyexcel_ods import get_data

#hashLinux = open('rc_fh.csv', 'r')
#hashLinux = open('rc_linux.csv', 'r')


def getListCommits():
    #file with the commits list that will be analyzed
    pathCommitsList = 'rc_errados.csv'
    hashLinux = open(pathCommitsList, 'r')
    linuxCommits = []
    for c in hashLinux:
        linuxCommits.append(c.strip())
        #print(c)
    return linuxCommits
