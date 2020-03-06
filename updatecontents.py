import codecs

htmlpath = [['home.html', 'index.html'], ['how-to-scramble/how-to-scramble.html', 'how-to-scramble/index.html'], ['policy/policy.html', 'policy/index.html'], ['request/request.html', 'request/index.html']]
replaceelements = [['menuformat.html', 'MENU_REPLACE_HERE']]

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy', 'FloppyGhost', 'Void', 'Kilominx']
for event in events:
    htmlpath.append([event + '/' + event + '.html', event + '/index.html'])

for path in htmlpath:
    for replacepath in replaceelements:
        print(path, replacepath)

        html = ''
        with codecs.open(path[0], 'r', 'utf-8', 'ignore') as f:
            html = f.read()
        
        replaceelement = ''
        with codecs.open(replacepath[0], 'r', 'utf-8', 'ignore') as f:
            replaceelement = f.read()
        
        #print(replacepath[1])
        html = html.replace(replacepath[1], replaceelement)
        #print(html)

        with codecs.open(path[1], 'w', 'utf-8', 'ignore') as f:
            f.write(html)