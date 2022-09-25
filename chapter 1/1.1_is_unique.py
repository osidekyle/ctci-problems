

def isUnique(string):
    # seenLetters = {}
    # for letter in string:
    #     if letter in seenLetters:
    #         return False
    #     else:
    #         seenLetters[letter] = 1
    # return True
    sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True



print(isUnique("yuhh"))