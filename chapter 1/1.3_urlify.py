




def urlify(url, trueLength):
    endIndex = len(url) - 1
    for i in range(trueLength - 1, -1, -1):
        if url[i] == " ":
            url[i: i + 3] = "%20"
            endIndex -= 3
        else:
            url[endIndex] = url[i]
            endIndex -= 1
    print(url)

urlify(["M", "r", " ", "J", "o", "h", "n", " ", "S", "m", "i", "t", "h", " ", " ", " ", " ", ], 13)


