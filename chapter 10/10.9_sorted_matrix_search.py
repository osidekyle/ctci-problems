

def sortedMatrixSearch(mat, target):
    # row = 0
    # col = len(mat[0]) - 1
    #
    #
    # while row < len(mat) and col >= 0:
    #     if mat[row][col] < target:
    #         row += 1
    #     elif mat[row][col] > target:
    #         col -= 1
    #     else:
    #         return (row, col)
    # return None

    def bstMat(mat, start, end, target):
        if start > end:
            return None
        mid = (start + end) // 2
        if mat[mid][0] > target:
            return bstMat(mat, start, mid, target)
        elif mat[mid][len(mat[mid]) - 1] < target:
            return bstMat(mat, mid + 1, end, target)
        elif mat[mid][0] < target and mat[mid][len(mat[mid]) - 1] > target:
            res = bstRow(mat[mid], 0, len(mat[mid]) - 1, target, mid)
            if res != None:
                return res

        tempStart, tempEnd = mid - 1, mid + 1
        while tempStart >= start and tempEnd <= end:
            if mat[tempStart][0] < target and mat[tempStart][len(mat[tempStart]) - 1] > target:
                res = bstRow(mat[tempStart], 0, len(mat[tempStart]) - 1, target, tempStart)
                if res != None:
                    return res

            if mat[tempEnd][0] < target and mat[tempEnd][len(mat[tempEnd]) - 1] > target:
                res = bstRow(mat[tempEnd], 0, len(mat[tempEnd]) - 1, target, tempEnd)
                if res != None:
                    return res

            tempStart -= 1
            tempEnd += 1

    def bstRow(arr, start, end, target, rowNum):
        if start >= end:
            return None
        mid = (start + end) // 2
        if arr[mid] == target:
            return (rowNum, mid)
        elif arr[mid] < target:
            return bstRow(arr, mid + 1, end, target, rowNum)
        else:
            return bstRow(arr, start, mid, target, rowNum)

    return bstMat(mat, 0, len(mat) - 1, target)



print(sortedMatrixSearch([[1, 2, 4, 5],
                         [2, 3, 5, 6],
                         [3, 7, 8, 9],
                         [4, 8, 9, 10]
                         ], 8))