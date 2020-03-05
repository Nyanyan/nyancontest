import csv
import os
import pandas as pd
import urllib.request
import time
def generatescramble(session):
    #res = subprocess.call('java -jar TNoodle-WCA-0.15.1.jar')
    #print(res)
    string = ['333', '222', '444', '555', '666', '777', '333ni', '333', 'clock', 'minx', 'pyram', 'skewb', 'sq1', '444ni', '555ni']
    response = urllib.request.urlopen('http://localhost:2014/scramble/.txt?e=' + string[session])
    scramble = response.read().decode('utf8', 'ignore').rstrip(os.linesep)
    scramble = ''.join(scramble.splitlines())
    response.close()
    #scramble = subprocess.check_output('curl "http://localhost:2014/scramble/.txt?e=' + string[session] + '"', shell=False).decode('utf8', 'ignore').rstrip(os.linesep)
    print(scramble)
    return scramble

with open('scramble.csv', mode='w') as f:
    f.write('')

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']
timeout = 10
events = [0, 1, 8, 13, 14]

for session in events:
    #session = 8 #clock
    row = [sessions[session]]
    while len(row) < 6:
        start = time.time()
        for i in range(1, 6):
            row.append(generatescramble(session))
            if time.time() - start > timeout:
                row = [sessions[session]]
                print('retry')
                time.sleep(10)
                break
    with open('scramble.csv', mode='a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(row)
    time.sleep(10)
print('finished generating scramble')
