import csv
import os
import pandas as pd
import urllib
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

sessions = ['3x3', '2x2', '4x4', '5x5', '6x6', '7x7', '3BLD', '3OH', 'Clock', 'Megaminx', 'Pyraminx', 'Skewb', 'Square-1', '4BLD', '5BLD']

session = 8 #clock
row = [sessions[session]]
for i in range(1, 6):
    row.append(generatescramble(session))
with open('scramble.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(row)