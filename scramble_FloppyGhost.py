import random

def stay_in_range(start, end, i):
    if i > end:
        i = start
    elif i < start:
        i = end
    return i


def rand_ex(start, end, ex):
    res = random.randint(start, end)
    shift = [-1, 1, 2][random.randrange(3)]
    if res in ex:
        res += shift
        res = stay_in_range(start, end, res)
    if res in ex:
        res += 1
        res = stay_in_range(start, end, res)
    return res

l = 20
scramble = ''
turn = ['U', 'UL', 'DR', 'DL', 'UR']
ex = []
exception = [set([0, 2]), set([0, 3]), set([1, 3]), set([1, 4]), set([2, 4])]
for i in range(l):
    index = rand_ex(0, 3, ex)
    scramble += turn[index] + '2 '
    ex.append(index)
    if not set(ex) in exception:
        ex = [index]
print(scramble, end='')

