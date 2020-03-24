import csv
import sys
import codecs

#make competition page

args = sys.argv
event = args[1]

html = ''
with codecs.open("competitionformat.html", 'r', 'utf-8', 'ignore') as f:
    html = f.read()

menu = ''
with codecs.open("menuformat.html", 'r', 'utf-8', 'ignore') as f:
    menu = f.read()

html = html.replace('MENU_REPLACE_HERE', menu)

html = html.replace('EVENT_REPLACE_HERE', event)

html = html.replace('ICON_REPLACE_HERE', '../images/' + event + '.png')

date = ''
with codecs.open("date.txt", 'r', 'utf-8', 'ignore') as f:
    date = f.read()
html = html.replace('DATE_REPLACE_HERE', date)

scramble = ''
scramblearr = []
with codecs.open("scramble.csv", 'r', 'utf-8', 'ignore') as f:
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

ranking = '<tr><td>順位</td><td>日時</td><td>名前</td><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td><td>平均</td></tr>'
rankingarr = []
with codecs.open(event + "/data.csv", 'r', 'utf-8', 'ignore') as f:
    rankingarr = list(csv.reader(f))
rank = 1
tmp = '0'
for i in range(len(rankingarr)):
    if tmp != rankingarr[i][7]:
        rank = i + 1
        tmp = rankingarr[i][7]
    ranking += '<tr><td>' + str(rank) + '</td>'
    for j in range(len(rankingarr[i])):
        if j == 1:
            ranking += '<td><a href=https://nyanyan.github.io/nyancontest/personaldata/' + str(rankingarr[i][j]) + '>' + str(rankingarr[i][j]) + '</a></td>'
        else:
            ranking += '<td>' + str(rankingarr[i][j]) + '</td>'
    ranking += '</tr>'
html = html.replace('RANKING_REPLACE_HERE', ranking)

yranking = '<tr><td>順位</td><td>日時</td><td>名前</td><td>1st</td><td>2nd</td><td>3rd</td><td>4th</td><td>5th</td><td>平均</td></tr>'
yrankingarr = []
with codecs.open(event + "/data_yesterday.csv", 'r', 'utf-8', 'ignore') as f:
    yrankingarr = list(csv.reader(f))
rank = 1
tmp = '0'
for i in range(len(yrankingarr)):
    if tmp != yrankingarr[i][7]:
        rank = i + 1
        tmp = yrankingarr[i][7]
    yranking += '<tr><td>' + str(rank) + '</td>'
    for j in range(len(yrankingarr[i])):
        if j == 1:
            yranking += '<td><a href=https://nyanyan.github.io/nyancontest/personaldata/' + str(yrankingarr[i][j]) + '>' + str(yrankingarr[i][j]) + '</a></td>'
        else:
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
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSfkW7bPcu3y2SMAJvAwWrnjh1Jcns1ioyAROAp6pgJqTu5VYw/formResponse"
    form = ["entry.1109233137", "entry.31162809", "entry.514623634", "entry.733409026", "entry.260491665", "entry.706137037"]
elif event == 'SuperFloppy':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdfngAyjbxqElCEQakGbSv8k17YMAv-mlyzS62dSh10MC79jA/formResponse"
    form = ["entry.1853627703", "entry.1755529497", "entry.307956320", "entry.869891293", "entry.2034438629", "entry.1023457257"]
elif event == 'FloppyGhost':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScccJcQL8eOObFQVDHhOEh6YF7_Qj_sbmJjUPIHXXKMF0Nhjw/formResponse"
    form = ["entry.1763240876", "entry.699565774", "entry.305741797", "entry.115360861", "entry.1967645681", "entry.776588168"]
elif event == 'Void':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdBqQWjQEvyQVozQiqUlZ9JtkxnicYEyFA9CZXE8VZMYmHNAA/formResponse"
    form = ["entry.1794443657", "entry.1331328678", "entry.657132955", "entry.1651365421", "entry.638295325", "entry.933075668"]
elif event == 'Kilominx':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSclB2rsUn14Pxoourpm7eBWDVNCCwDqxV4Z5y8C1KkhiTl2TQ/formResponse"
    form = ["entry.278586755", "entry.1763082143", "entry.1827584236", "entry.949458588", "entry.284447102", "entry.1636857682"]
elif event == 'Redi':
    googleform = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSehDFzt91aMwTPWVozLIlqPC7xRrfoNLcun_Z9s-jRlA4bCow/formResponse"
    form = ["entry.1740381961", "entry.1778933736", "entry.1688742736", "entry.1076503294", "entry.1511718114", "entry.729104288"]
else:
    googleform = ""
    form = ["entry.", "entry.", "entry.", "entry.", "entry.", "entry."]
html = html.replace('GOOGLEFORM_REPLACE_HERE', '"' + googleform + '"')
html = html.replace('NAME_REPLACE_HERE', '"' + form[0] + '"')
for i in range(1, len(form)):
    html = html.replace(str(i) + '_REPLACE_HERE', '"' + form[i] + '"')



with codecs.open(event + "/index.html", 'w', 'utf-8', 'ignore') as f:
    f.write(html)
