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

l = 15
scramble = ''
ex = []
turn = ['R', 'F', 'L', 'B']
for i in range(l):
    index = rand_ex(0, 3, ex)
    scramble += turn[index] + '2 '
    ex.append(index)
    if set(ex) != set([0, 1]) and set(ex) != set([2, 3]):
        ex = [index]
print(scramble, end='')
