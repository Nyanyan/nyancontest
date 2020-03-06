import csv
import os
import pandas as pd
import urllib.request
import time
import subprocess

def generatescramble(i):
    #res = subprocess.call('java -jar TNoodle-WCA-0.15.1.jar')
    #print(res)
    string = ['333', '222', '444', '555', '666', '777', '333ni', '333', 'clock', 'minx', 'pyram', 'skewb', 'sq1', '444ni', '555ni']
    response = urllib.request.urlopen('http://localhost:2014/scramble/.txt?e=' + string[i])
    scramble = response.read().decode('utf8', 'ignore').rstrip(os.linesep)
    scramble = ''.join(scramble.splitlines())
    response.close()
    #scramble = subprocess.check_output('curl "http://localhost:2014/scramble/.txt?e=' + string[session] + '"', shell=False).decode('utf8', 'ignore').rstrip(os.linesep)
    print(scramble)
    return scramble

with open('scramble.csv', mode='w') as f:
    f.write('')

wca = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
events = ['Clock', 'Mirror3x3', 'Floppy']
timeout = 10
scrambleevent = [8, 0, 15]

for i in range(len(events)):
    #session = 8 #clock
    row = [events[i]]
    if scrambleevent[i] < 15:
        while len(row) < 6:
            start = time.time()
            for _ in range(1, 6):
                row.append(generatescramble(scrambleevent[i]))
                if time.time() - start > timeout:
                    row = [events[i]]
                    print('retry')
                    time.sleep(10)
                    break
        time.sleep(10)
    else:
        command = ['python', 'scramble_' + events[i] + '.py']
        for j in range(5):
            row.append(subprocess.check_output(command).decode())
            print(row[j+1])
    with open('scramble.csv', mode='a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(row)
print('finished generating scramble')
