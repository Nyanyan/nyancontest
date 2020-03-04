import datetime
dt_now = datetime.datetime.now()
date = str(dt_now.year) + '年' + str(dt_now.month) + '月' + str(dt_now.day) + '日'
with open('date.txt', mode='w') as f:
    f.write(date)