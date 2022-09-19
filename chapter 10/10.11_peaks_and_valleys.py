


def peaksAndValleys(nums):
    def maxIndex(nums, a, b, c):
        numA = a if a >=0 and a < len(nums) else float("inf") * -1
        numB = b if b >=0 and b < len(nums) else float("inf") * -1
        numC = c if c >=0 and c < len(nums) else float("inf") * -1

        maxNum = max(numA, numB, numC)
        if maxNum == numA:
            return a
        elif maxNum == numB:
            return b
        else:
            return c

    def swap(nums, i1, i2):
        temp = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = temp

    for i in range(1, len(nums), 2):
        maxIndexVal = maxIndex(nums, i - 1, i, i + 1)
        swap(nums, i, maxIndexVal)
    return nums

print(peaksAndValleys([5, 3, 1, 2, 3]))
