import csv
import sys

args = sys.argv
event = args[1]

html = ''
with open("competitionformat.html", mode='r') as f:
    html = f.read()
#html = html.replace('SCRIPT_REPLACE_HERE', '            <script src="getdata.js"></script>\n            <script src="getdata_yesterday.js"></script>\n          <script src="getdate.js"></script>\n            <script src="getscramble.js"></script>')

html = html.replace('EVENT_REPLACE_HERE', event)

html = html.replace('ICON_REPLACE_HERE', '../images/' + event + '.png')

date = ''
with open("date.txt", mode='r') as f:
    date = f.read()
html = html.replace('DATE_REPLACE_HERE', date)

scramble = ''
scramblearr = []
with open("scramble.csv", mode='r') as f:
    scramblearr = list(csv.reader(f))
flag = False
for i in range(len(scramblearr)):
    if scramblearr[i][0] == event:
        flag = True
    if flag:
        for j in range(len(scramblearr[i])):
            scramble += '<tr><td>' + str(scramblearr[i][j]) + '</td></tr>'
        break
html = html.replace('SCRAMBLE_REPLACE_HERE', scramble)

ranking = ''
rankingarr = []
with open(event + "/data.csv", mode='r') as f:
    rankingarr = list(csv.reader(f))
for i in range(len(rankingarr)):
    ranking += '<tr>'
    for j in range(len(rankingarr[i])):
        ranking += '<td>' + str(rankingarr[i][j]) + '</td>'
    ranking += '</tr>'
html = html.replace('RANKING_REPLACE_HERE', ranking)

yranking = ''
yrankingarr = []
with open(event + "/data_yesterday.csv", mode='r') as f:
    yrankingarr = list(csv.reader(f))
for i in range(len(yrankingarr)):
    yranking += '<tr>'
    for j in range(len(yrankingarr[i])):
        yranking += '<td>' + str(yrankingarr[i][j]) + '</td>'
    yranking += '</tr>'
html = html.replace('RANKINGYESTERDAY_REPLACE_HERE', yranking)

if event == 'Clock':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdNs5H8dzfoZe0IWXMx4AujhDipY2MYe6LoJtdKusxlNN1QWA/formResponse"
    form = ["entry.1460875154", "entry.39328532", "entry.975282763", "entry.673200780", "entry.1826089930", "entry.75959801"]
elif event == 'Mirror3x3':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfec5JC5vKDGeuY31i82-wS7h2bOz0a80K66ExTVK_AW-BU1w/formResponse"
    form = ["entry.124718628", "entry.595343204", "entry.772823004", "entry.967262556", "entry.1547065456", "entry.1566696308"]
elif event == 'Floppy':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfec5JC5vKDGeuY31i82-wS7h2bOz0a80K66ExTVK_AW-BU1w/formResponse"
    form = ["entry.124718628", "entry.595343204", "entry.772823004", "entry.967262556", "entry.1547065456", "entry.1566696308"]
html = html.replace('GOOGLEFORM_REPLACE_HERE', '"' + googleform + '"')
html = html.replace('NAME_REPLACE_HERE', '"' + form[0] + '"')
for i in range(1, len(form)):
    html = html.replace(str(i) + '_REPLACE_HERE', '"' + form[i] + '"')



with open(event + "/index.html", mode='w') as f:
    f.write(html)
