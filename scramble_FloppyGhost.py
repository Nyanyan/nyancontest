import random

def rand_ex(start, end, ex):
    res = random.randint(start, end)
    shift = random.randint(0, 1) * randint(2, 3) - 1
    while res in ex:
        res += shift
        if res > end:
            res = start
        elif res < start:
            res = end
    return res

l = 20
scramble = ''
turn = ['U', 'UL', 'DR', 'DL', 'UR']
ex = []
for i in range(l):
    index = rand_ex(0, 3, ex)
    scramble += turn[index] + '2 '
    ex.append(index)
    if set(ex) != set([0, 2]) and set(ex) != set([0, 3]) and set(ex) != set([1, 3]) and set(ex) != set([1, 4]) and set(ex) != set([2, 4]):
        ex = [index]
print(scramble, end='')
