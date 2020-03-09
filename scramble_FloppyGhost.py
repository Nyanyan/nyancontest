import random

def stay_in_range(start, end, i):
    if i > end:
        a = i - end
        i = start + a - 1
    elif i < start:
        a = start - i
        i = end - a + 1
    return i


def rand_ex(start, end, ex):
    arr = list(range(start, end + 1))
    i = 0
    while i < len(arr):
        if arr[i] in ex:
            del arr[i]
            i -= 1
        i += 1
    res = arr[random.randrange(len(arr))]
    return res

l = 20
scramble = ''
turn = ['U', 'UR', 'DR', 'DL', 'UL']
ex = []
exception = [set([0, 2]), set([0, 3]), set([1, 3]), set([1, 4]), set([2, 4])]
for i in range(l):
    index = rand_ex(0, 4, ex)
    scramble += turn[index] + '2 '
    ex.append(index)
    flag = True
    keep = []
    if len(ex) == 3:
        flag = False
        keep.append(ex[2])
        ex.sort()
        for j in range(3):
            tmp = []
            deletetmp = 0
            for k in range(2):
                if stay_in_range(0, 4, ex[stay_in_range(0, 2, j + k)] + 1) != ex[stay_in_range(0, 2, j + k + 1)]:
                    tmp.append(False)
                else:
                    tmp.append(True)
            if tmp[0] and tmp[1]:
                flag = True
                break
            elif not tmp[0] and not tmp[1]:
                keep.append(ex[stay_in_range(0, 2, j + 1)])
    if not set(ex) in exception and flag:
        ex = [index]
    elif not set(ex) in exception and not flag:
        ex = keep
print(scramble, end='')

