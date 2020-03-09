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

l = 20
scramble = ''
turn = ['R', 'F', 'L', 'B']
direction = ['2', '', "'"]
ex = []
exception = [set([0, 2]), set([1, 3])]
for i in range(l):
    index1 = rand_ex(0, 3, ex)
    index2 = random.randint(0, 2)
    scramble += turn[index1] + direction[index2] + ' '
    ex.append(index1)
    if not set(ex) in exception:
        ex = [index1]
print(scramble, end='')
