import csv
html = ''
with open("../competitionformat.html", 'r',encoding="cp932") as f:
    html = f.read()
#html = html.replace('SCRIPT_REPLACE_HERE', '            <script src="getdata.js"></script>\n            <script src="getdata_yesterday.js"></script>\n          <script src="getdate.js"></script>\n            <script src="getscramble.js"></script>')
scramble = ''
scramblearr = []
with open("../scramble.csv", 'r', encoding="cp932") as f:
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
with open("index.html", 'w', encoding="cp932") as f:
    f.write(html)