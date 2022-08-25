





def permutationWithDups(string):
    res = []
    freqHashMap = generateFrequencyTable(string)
    genPerms(freqHashMap, "", len(string), res)
    return res

def genPerms(freqHashMap, prefix, remaining, result):
    if remaining == 0:
        result.append(prefix)
        return

    for char in freqHashMap:
        count = freqHashMap[char]
        if count > 0:
            freqHashMap[char] = count - 1
            genPerms(freqHashMap, prefix + char, remaining - 1, result)
            freqHashMap[char] = count


def generateFrequencyTable(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


print(permutationWithDups("aaaaaaaaaaaaaab"))
