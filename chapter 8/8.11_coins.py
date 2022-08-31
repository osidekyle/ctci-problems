def coinsWrapper(cents):

    count = [-1] * cents
    def coins(cents, numCoins):
        if cents == 0:
            if count[numCoins - 1] != -1:
                return 0
            else:
                count[numCoins - 1] = 1
                return 1
        if cents < 0:
            return 0

        res = coins(cents - 1, numCoins + 1) + coins(cents - 5, numCoins + 1) + coins(cents - 10, numCoins + 1) + coins(cents - 25, numCoins + 1)

        return res

    print(coins(cents, 0))

coinsWrapper(10)