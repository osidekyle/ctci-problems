

def checkPermutation(string1, string2):
    letters = {}

    for letter in string1:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in string2:
        if letter not in letters:
            return False
        elif letters[letter] == 0:
            return False
        else:
            letters[letter] -= 1

    for value in letters.values():
        if value != 0:
            return False

    return True

print(checkPermutation("aba", "baa"))