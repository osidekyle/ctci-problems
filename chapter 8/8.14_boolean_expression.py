

def stringToBool(string):
    return True if string == "1" else False

def countEval(string, result):
    if len(string) == 0:
        return 0
    if len(string) == 1:
        if stringToBool(string) == result:
            return 1
        else:
            return 0

    ways = 0

    for i in range(1, len(string), 2):
        c = string[i]
        left = string[:i]
        right = string[i + 1:]

        leftTrue = countEval(left, True)
        leftFalse = countEval(left, False)
        rightTrue = countEval(right, True)
        rightFalse = countEval(right, False)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)

        totalTrue = 0
        if c == "^":
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        elif c == "&":
            totalTrue = leftTrue * rightTrue
        elif c == "|":
            totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse


        subways = totalTrue if result else total - totalTrue

        ways += subways

    return ways

print(countEval("1^0|0|1", False))