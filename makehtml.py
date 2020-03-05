import csv
<<<<<<< HEAD:makehtml.py
<<<<<<< HEAD:makehtml.py
import sys

args = sys.argv
event = args[1]

=======
>>>>>>> parent of f5e9350... cleaning:clock/makehtml.py
=======
>>>>>>> parent of f5e9350... cleaning:clock/makehtml.py
html = ''
with open("competitionformat.html", 'r',encoding="utf-8") as f:
    html = f.read()
#html = html.replace('SCRIPT_REPLACE_HERE', '            <script src="getdata.js"></script>\n            <script src="getdata_yesterday.js"></script>\n          <script src="getdate.js"></script>\n            <script src="getscramble.js"></script>')

<<<<<<< HEAD:makehtml.py
<<<<<<< HEAD:makehtml.py
=======
event = 'Clock'
>>>>>>> parent of f5e9350... cleaning:clock/makehtml.py
=======
event = 'Clock'
>>>>>>> parent of f5e9350... cleaning:clock/makehtml.py
html = html.replace('EVENT_REPLACE_HERE', event)

date = ''
with open("date.txt", 'r', encoding="utf-8") as f:
    date = f.read()
html = html.replace('DATE_REPLACE_HERE', date)

scramble = ''
scramblearr = []
with open("scramble.csv", 'r', encoding="utf-8") as f:
    scramblearr = list(csv.reader(f))
flag = False
for i in range(len(scramblearr)):
    if scramblearr[i][0] == 'Clock':
        flag = True
    if flag:
        for j in range(len(scramblearr[i])):
            scramble += '<tr><td>' + str(scramblearr[i][j]) + '</td></tr>'
        break
html = html.replace('SCRAMBLE_REPLACE_HERE', scramble)

ranking = ''
rankingarr = []
with open(event + "/data.csv", 'r', encoding="utf-8") as f:
    rankingarr = list(csv.reader(f))
for i in range(len(rankingarr)):
    ranking += '<tr>'
    for j in range(len(rankingarr[i])):
        ranking += '<td>' + str(rankingarr[i][j]) + '</td>'
    ranking += '</tr>'
html = html.replace('RANKING_REPLACE_HERE', ranking)

yranking = ''
yrankingarr = []
with open(event + "/data_yesterday.csv", 'r', encoding="utf-8") as f:
    yrankingarr = list(csv.reader(f))
for i in range(len(yrankingarr)):
    yranking += '<tr>'
    for j in range(len(yrankingarr[i])):
        yranking += '<td>' + str(yrankingarr[i][j]) + '</td>'
    yranking += '</tr>'
html = html.replace('RANKINGYESTERDAY_REPLACE_HERE', yranking)



with open("index.html", 'w', encoding="utf-8") as f:
    f.write(html)