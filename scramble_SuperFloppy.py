import random
import copy
l = 20
scramble = ''
turn = ['R', 'L', 'F', 'B']
direction = ['2', '', "'"]
tmp1 = random.randint(0, 3)
tmp2 = random.randint(0, 2)
scramble += turn[tmp1] + direction[tmp2] + ' '
select = copy.deepcopy(turn)
del select[tmp1]
for i in range(l-1):
    tmp1 = random.randint(0, 2)
    tmp2 = random.randint(0, 2)
    add = select[tmp1]
    scramble += add + direction[tmp2] + ' '
    select = copy.deepcopy(turn)
    for j in range(4):
        if add == select[j]:
            del select[j]
            break
print(scramble, end='')
