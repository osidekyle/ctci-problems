def permutationWithoutDups(string):

    permutations = []
    if len(string) == 0:
        permutations.append("")
        return permutations


    first = string[0]
    remainder = string[1:]
    words = permutationWithoutDups(remainder)

    for word in words:
        for j in range(len(word) + 1):
            permutations.append(word[:j] + first + word[j:])

    return permutations

print(permutationWithoutDups("abc"))
