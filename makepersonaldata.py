import csv
import sys
import codecs
import os
import copy

#make personal data page

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy', 'FloppyGhost', 'Void', 'Kilominx', 'Redi']

for event in events:
    rankingarr = []
    with codecs.open(event + "/data.csv", 'r', 'utf-8', 'ignore') as f:
        rankingarr = list(csv.reader(f))
    rank = 1
    tmp = '0'
    for i in range(len(rankingarr)):
        ranking_person = ''
        if tmp != rankingarr[i][7]:
            rank = i + 1
            tmp = rankingarr[i][7]
        ranking_person += '<tr><td>' + str(rank) + '</td>'
        for j in range(len(rankingarr[i])):
            if j == 1:
                continue
            ranking_person += '<td>' + str(rankingarr[i][j]) + '</td>'
        ranking_person += '</tr>'
        os.makedirs('personaldata/' + rankingarr[i][1] + '/', exist_ok=True)
        try:
            with open('personaldata/' + rankingarr[i][1] + '/' + event + '.html', mode='x', encoding='utf-8') as f:
                f.write('<tr><td>順位</td><td>日時</td><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td><td>平均</td></tr>' + ranking_person)
            with open('personaldata/list.txt', mode='a', encoding='utf-8') as f:
                f.write(rankingarr[i][1] + '\n')
        except FileExistsError:
            with open('personaldata/' + rankingarr[i][1] + '/' + event + '.html', mode='a', encoding='utf-8') as f:
                f.write(ranking_person)

personlist = []
with open('personaldata/list.txt', mode='r', encoding='utf-8') as f:
    personlist = list(f.read().split('\n'))
del personlist[-1]
print(personlist)
html = ''
with open('personalpages.html', mode='r', encoding='utf-8') as f:
    html = f.read()
menu = ''
with codecs.open("menuformat.html", 'r', 'utf-8', 'ignore') as f:
    menu = f.read()
for person in personlist:
    html_person = copy.deepcopy(html)
    html_person = html_person.replace('NAME_REPLACE_HERE', person)
    html_person = html_person.replace('MENU_REPLACE_HERE', menu)
    for event in events:
        try:
            with open('personaldata/' + person + '/' + event + '.html', mode='x', encoding='utf-8') as f:
                f.write('<tr><td>順位</td><td>日時</td><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td><td>平均</td></tr>')
        except:
            pass
        data = ''
        with open('personaldata/' + person + '/' + event + '.html', mode='r', encoding='utf-8') as f:
            data = f.read()
        html_person = html_person.replace(event + '_REPLACE_HERE', data)
    with open('personaldata/' + person + '/index.html', mode='w', encoding='utf-8') as f:
        f.write(html_person)

personhtml = ''
for person in personlist:
    personhtml += '<a href=https://nyanyan.github.io/nyancontest/personaldata/' + person + '>' + person + '</a>\n\n'
html_personaltop = ''
with open('personaldata/index.html', mode='r', encoding='utf-8') as f:
    html_personaltop = f.read()
html_personaltop = html_personaltop.replace('PERSONALPAGE_REPLACE_HERE', personhtml)
with open('personaldata/index.html', mode='w', encoding='utf-8') as f:
    f.write(html_personaltop)