import random
import copy
l = 20
scramble = ''
turn = ['U', 'UL', 'UR', 'DL', 'DR']
tmp = random.randint(0, 4)
scramble += turn[tmp] + '2 '
select = copy.deepcopy(turn)
del select[tmp]
for i in range(l-1):
    tmp = random.randint(0, 3)
    add = select[tmp]
    scramble += add + '2 '
    select = copy.deepcopy(turn)
    for j in range(4):
        if add == select[j]:
            del select[j]
            break
print(scramble, end='')
