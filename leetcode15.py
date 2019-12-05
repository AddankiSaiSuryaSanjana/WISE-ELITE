def zeroSumTriplets(array):
    triplet, zeroSumtriplet = [], []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            k = - array[i] - array[j]
            if k in array:
                triplet.append([array[i], array[j], k])
    for i in triplet:
        i.sort()
        if i not in zeroSumtriplet:
            zeroSumtriplet.append(i)
    return zeroSumtriplet
        
print(zeroSumTriplets([-1, 0, 1, -1, 4, 2]))
