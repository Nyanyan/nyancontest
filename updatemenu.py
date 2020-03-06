import codecs

htmlpath = [['home.html', 'index.html']]
replaceelements = [['menuformat.html', 'MENU_REPLACE_HERE']]

for path, replacepath in zip(htmlpath, replaceelements):
    print(path, replacepath)
    html = ''
    with codecs.open(path[0], 'r', 'utf-8', 'ignore') as f:
        html = f.read()
    replaceelement = ''
    with codecs.open(replacepath[0], 'r', 'utf-8', 'ignore') as f:
        replaceelement = f.read()
    html.replace(replacepath[1], replaceelement)

    with codecs.open(path[1], 'w', 'utf-8', 'ignore') as f:
        f.write(html)