



def stackOfBoxes(n, w, h, d):
    def checkValid(index, w, h, d, stack):
        if len(stack) == 0:
            return True

        lastWidth = w[stack[-1]]
        lastHeight = h[stack[-1]]
        lastDepth = d[stack[-1]]

        if w[index] < lastWidth and h[index] < lastHeight and d[index] < lastDepth:
            return True
        return False


    def stackMaker(n, w, h, d, stack, currMax):
        newMax = 0
        for i in range(n):
            if i not in stack and checkValid(i, w, h, d, stack):
                stack.append(i)
                newMax = max(newMax, stackMaker(n, w, h, d, stack, currMax + 1))
                stack.pop()

        return max(currMax, newMax)

    return stackMaker(n, w, h, d, [], 0)



print(stackOfBoxes(4, [1, 2, 3, 2.5], [1, 2, 3, 2.5], [1, 2, 3, 2.5]))



