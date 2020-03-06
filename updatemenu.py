import codecs

htmlpath = [['home.html', 'index.html']]

for path in htmlpath:
    html = ''
    with codecs.open("competitionformat.html", 'r', 'utf-8', 'ignore') as f:
        html = f.read()