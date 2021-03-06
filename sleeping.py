import codecs

htmlpaths = ['index.html']
replaceelements = [['menuformat.html', 'MENU_REPLACE_HERE']]

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy', 'FloppyGhost', 'Void', 'Kilominx', 'Redi']
for event in events:
    htmlpaths.append(event + '/index.html')

html = ''
with codecs.open('sleeping.html', 'r', 'utf-8', 'ignore') as f:
    html = f.read()
for htmlpath in htmlpaths:
    print(htmlpath)
    if len(htmlpath) > 11:
        html = html.replace('"images', '"../images')
        html = html.replace('"assets', '"../assets')
    for replacepath in replaceelements:
        replaceelement = ''
        with codecs.open(replacepath[0], 'r', 'utf-8', 'ignore') as f:
            replaceelement = f.read()
        html = html.replace(replacepath[1], replaceelement)

        with codecs.open(htmlpath, 'w', 'utf-8', 'ignore') as f:
            f.write(html)
