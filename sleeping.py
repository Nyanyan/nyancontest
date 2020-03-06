import codecs

htmlpaths = ['index.html', 'how-to-scramble/index.html', 'policy/index.html', 'request/index.html']

html = ''
with codecs.open('sleeping.html', 'r', 'utf-8', 'ignore') as f:
    html = f.read()
for htmlpath in htmlpaths:
    with codecs.open(htmlpath, 'w', 'utf-8', 'ignore') as f:
        f.write(html)