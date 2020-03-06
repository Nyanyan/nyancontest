import random

len = 30
delimiter = ' / '

scramble = ''
direction = ['++', '--']
direction_u = ['', "'"]

for i in range(1, len + 1):
    if i % 2 == 0:
        scramble += 'D'
    else:
        scramble += 'R'

    scramble += random.choice(direction) + ' '

    if i % 10 == 0:
        scramble += 'U' + random.choice(direction_u)
        if i != len:
            scramble += delimiter

print(scramble, end='')
