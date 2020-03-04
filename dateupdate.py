import datetime
dt_now = datetime.datetime.now()
date = str(dt_now.year) + '/' + str(dt_now.month) + '/' + str(dt_now.day)
with open('date.txt', mode='w') as f:
    f.write(date)