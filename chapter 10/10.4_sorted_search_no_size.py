class Listy:
    def __init__(self):
        self.nums = [2, 3, 5, 9, 14]


    def get(self, index):
        if index >= 0 and index < len(self.nums):
            return self.nums[index]
        else:
            return -1


def sortedSearchNoSize(listy, target):
    length = 0
    while listy.get(length) != -1:
        length += 1


    def bst(start, end, listy, target):
        if start > end:
            return None
        mid = (start + end) // 2

        found = listy.get(mid)
        if found == target:
            return mid
        elif found < target:
            return bst(mid + 1, end, listy, target)
        else:
            return bst(start, mid, listy, target)

    return bst(0, length, listy, target)

print(sortedSearchNoSize(Listy(), 3))