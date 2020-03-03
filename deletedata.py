import csv
with open('clock/data.csv', mode='w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow([])