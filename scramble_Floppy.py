import random

def rand_ex(start, end, ex):
    res = random.randint(start, end)
    print(res in ex, res, ex)
    while res in ex:
        res += 1
        if res > end:
            res = start
    return res

l = 15
scramble = ''
ex = []
turn = ['R', 'L', 'F', 'B']
for i in range(l):
    index = rand_ex(0, 3, ex)
    scramble += turn[index] + '2 '
    flag = True
    ex.append(index)
    if set(ex) != set([0, 1]) and set(ex) != set([2, 3]):
        ex = [index]
print(scramble, end='')
