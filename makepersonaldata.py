import csv
import sys
import codecs
import os

#make personal data page

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy', 'FloppyGhost', 'Void', 'Kilominx', 'Redi']

for event in events:
    rankingarr = []
    with codecs.open(event + "/data.csv", 'r', 'utf-8', 'ignore') as f:
        rankingarr = list(csv.reader(f))
    rank = 1
    tmp = '0'
    for i in range(len(rankingarr)):
        ranking_person = '<tr><td>順位</td><td>日時</td><td>名前</td><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td><td>平均</td></tr>'
        if tmp != rankingarr[i][7]:
            rank = i + 1
            tmp = rankingarr[i][7]
        ranking += '<tr><td>' + str(rank) + '</td>'
        for j in range(len(rankingarr[i])):
            ranking += '<td>' + str(rankingarr[i][j]) + '</td>'
        ranking += '</tr>'
        os.makedirs(new_dir_path_recursive, exist_ok=True)
    html = html.replace('RANKING_REPLACE_HERE', ranking)