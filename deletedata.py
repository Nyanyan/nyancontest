import csv

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
#events = [0, 1, 8, 13, 14]
events = [8]

for i in events:
    event = sessions[i]
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
