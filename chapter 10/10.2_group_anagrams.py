

def getValue(string):
    return sum(map(ord, string))

def merge(strings, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = strings[left + i]

    for i in range(n2):
        R[i] = strings[right + i]

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if getValue(L[i]) < getValue(R[j]):
            strings[k] = L[i]
            i += 1
        else:
            strings[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        strings[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        strings[k] = R[j]
        j += 1
        k += 1

def mergeSort(strings, l, r):
    if l < r:
        mid = l + (r - l) // 2
        mergeSort(strings, l, mid)
        mergeSort(strings, mid + 1, r)
        merge(strings, l, mid, r)

def groupAnagrams(strings):
    mergeSort(strings, 0, len(strings) - 1)



words = ["aba", "ccc", "baa"]
groupAnagrams(words)
print(words)