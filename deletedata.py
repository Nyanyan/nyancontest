import csv

events = ['Clock', 'Mirror3x3', 'Floppy']

for event in events:
    data = []
    with open(event + '/data.csv', mode='r') as f:
        tmp = f.readline()
        while len(tmp):
            tmp = list(tmp.split(','))
            tmp[len(tmp) - 1] = tmp[len(tmp) - 1][:len(tmp[len(tmp) - 1]) - 1]
            data.append(tmp)
            tmp = f.readline()
    with open(event + '/data_yesterday.csv', mode='w') as f:
        writer = csv.writer(f, lineterminator='\n')
        for i in range(len(data)):
            writer.writerow(data[i])
    with open(event + '/data.csv', mode='w') as f:
        f.write('')
print('finish deleting data')
