


def parens(n):

    res = []


    def genParens(balance, built):
        if len(built)/2 == n:
            if balance == 0:
                res.append(built)
            return
        if balance < 0:
            return
        genParens(balance + 1, built + "(")
        genParens(balance - 1, built + ")")

    genParens(0, "")

    return res

print(parens(3))