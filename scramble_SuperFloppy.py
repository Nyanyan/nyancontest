import random

def rand_ex(start, end, ex):
    res = random.randint(start, end)
    shift = random.randint(0, 1) * 2 - 1
    while res in ex:
        res += shift
        if res > end:
            res = start
        elif res < start:
            res = end
    return res

l = 20
scramble = ''
turn = ['R', 'F', 'L', 'B']
direction = ['2', '', "'"]
ex = []
for i in range(l):
    index1 = rand_ex(0, 3, ex)
    index2 = random.randint(0, 2)
    scramble += turn[index1] + direction[index2] + ' '
    ex.append(index1)
    if set(ex) != set([0, 1]) and set(ex) != set([2, 3]):
        ex = [index1]
print(scramble, end='')
