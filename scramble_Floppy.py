import random

def rand_ex(start, end, ex):
    arr = list(range(start, end + 1))
    i = 0
    while i < len(arr):
        if arr[i] in ex:
            del arr[i]
        else:
            i += 1
    res = arr[random.randrange(len(arr))]
    return res

l = 15
scramble = ''
ex = []
turn = ['R', 'F', 'L', 'B']
exception = [set([0, 2]), set([1, 3])]
for i in range(l):
    index = rand_ex(0, 3, ex)
    scramble += turn[index] + '2 '
    ex.append(index)
    if not set(ex) in exception:
        ex = [index]
print(scramble, end='')
