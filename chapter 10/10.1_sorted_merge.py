




def sortedMerge(a, b, countA, countB):
    index = countA + countB - 1
    indexA = countA - 1
    indexB = countB - 1

    while indexB >= 0:
        if indexA >= 0 and a[indexA] > b[indexB]:
            a[index] = a[indexA]
            indexA -= 1
        else:
            a[index] = b[indexB]
            indexB -= 1
        index -= 1

    return a

print(sortedMerge([1, 3, 5, -1, -1], [2, 4], 3, 2))