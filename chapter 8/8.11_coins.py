def coinsWrapper(cents):
    coinMap = [[-1] * 4 for x in range(cents + 1)]

    # def coins(cents, numCoins):
    #     if cents == 0:
    #         if count[numCoins - 1] != -1:
    #             return 0
    #         else:
    #             count[numCoins - 1] = 1
    #             return 1
    #     if cents < 0:
    #         return 0
    #
    #     res = coins(cents - 1, numCoins + 1) + coins(cents - 5, numCoins + 1) + coins(cents - 10, numCoins + 1) + coins(cents - 25, numCoins + 1)
    #
    #     return res
    #

    def coins(total, index, coinMap, denoms):
        if coinMap[total][index] != -1:
            return coinMap[total][index]

        coin = denoms[index]
        if index == len(denoms) - 1:
            remainder = total % coin
            if remainder == 0:
                return 1
            else:
                return 0

        numberOfWays = 0
        for i in range(0, total + 1, coin):
            numberOfWays += coins(total - i, index + 1, coinMap, denoms)

        coinMap[total][index] = numberOfWays
        return numberOfWays


    print(coins(cents, 0, coinMap, [1, 5, 10, 25]))

coinsWrapper(10)