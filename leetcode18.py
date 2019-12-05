def zeroSumQuadraplets(array, target):
    quadraplet, zeroSumquadraplet = [], []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            for k in range(j + 1, len(array)):
                p = target - array[i] - array[j] - array[k]
                if p in array:
                    quadraplet.append([array[i], array[j], array[k], p])
    for i in quadraplet:
        i.sort()
        if i not in zeroSumquadraplet:
            zeroSumquadraplet.append(i)
    return zeroSumquadraplet
        
print(zeroSumQuadraplets([1, 0, -1, 0, -2, 2], 1))

