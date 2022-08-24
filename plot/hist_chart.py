# import plotly.express as px
from pydriller import Repository
from pathlib import Path, PureWindowsPath
import datetime
import seaborn as sns

pattern = 'Remove Feature'
fileName = "input/{}.txt".format(pattern)
# filePath = ".{}".format(fileName)
# fileToOpen = Path(filePath)
linuxRepo = "..\..\linux_repo\linux"

commitList = [
    "4b08478422040ae8cb11acc15d51f1cdb0ac39c8",
    "77da71b3a03ebb2bd06500ca1d85e1c5083bb005",
    "dd9589c7c00ab41e49d972dc9a01fcac7dc39961",
    "136dfa5edae3207422a8b93347eb79e92e07cdfa",
    "7d7ee958867ad3c9c829a36c56e870879e83391f",
    "e66f233dc7f7aef51d82cac1b93b46f7c9bf42ef",
    "dfcc11ad4a4e620440475e25cf75d10c9d3bf7c2",
    "95807689eab8441737572d1a9daaa1025429a908",
    "97411608fd5f17735f51103da08a738be1f932d9",
    "06ff74fd197aa8205443cf64b94383802602e320",
    "a6e95a86e02e4a60b4355c84d19dba2baf3d87ba",
    "e55f7cd2467631980f749fb0aef197c06ce38d6a"
]


def parsingTXTtoList(fileToOpen):
    commits = []
    txtHashes = open(fileToOpen, 'r')
    for hash in txtHashes:
        commits.append(hash.strip())
    return commits


# listaCommits = parsingTXTtoList(fileName)

def formating_date(date):
    date_formated = str(date).strip().split('-')
    return date_formated


outputListCommit = ['{},{},{},{}'.format("pattern", "commit", "date", "count")]

for commit in Repository(linuxRepo, since=datetime.datetime(2013, 1, 1), to=datetime.datetime(2014, 1, 1), only_commits=commitList).traverse_commits():
    date = formating_date(commit.committer_date)
    # if(commit.merge == True):
    #     pass
    # else:
    #     row = '{},{},{},{}'.format(pattern, commit.hash,
    #                            '{}-{}'.format(date[0], date[1]), 1)
    #     outputListCommit.append(row)
    #     print(row)
    row = '{},{},{},{}'.format(
        pattern, commit.hash, '{}-{}'.format(date[0], date[1]), 1)
    outputListCommit.append(row)
    print(row)

fileNameOutput = "plot/output/{}.csv".format(pattern)
writer = open(fileNameOutput, 'w')

for row in outputListCommit:
    writer.write('{}\n'.format(row))
