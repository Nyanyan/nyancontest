import csv
import codecs

events = ['Clock', 'Mirror3x3', 'Floppy', 'SuperFloppy']

for event in events:
    data = []
    with codecs.open(event + '/data.csv', 'r', 'utf-8', 'ignore') as f:
        tmp = f.readline()
        while len(tmp):
            tmp = list(tmp.split(','))
            tmp[len(tmp) - 1] = tmp[len(tmp) - 1][:len(tmp[len(tmp) - 1]) - 1]
            data.append(tmp)
            tmp = f.readline()
    with codecs.open(event + '/data_yesterday.csv', 'w', 'utf-8', 'ignore') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(len(data)):
            writer.writerow(data[i])
    with codecs.open(event + '/data.csv', 'w', 'utf-8', 'ignore') as f:
        f.write('')
print('finish deleting data')
