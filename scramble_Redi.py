import random

len = 8

scramble = ''
turn = ['L', 'R']
direction = ['', "'"]

for i in range(len):
    first = random.randint(0, 1)
    for j in range(3 + random.randint(0, 3)):
        scramble += turn[(first + j) % 2] + random.choice(direction) + ' '
    scramble += 'x '

scramble = scramble[:-3]
print(scramble, end='')