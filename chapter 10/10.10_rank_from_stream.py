





class RankedNode:
    def __init__(self, d):
        self.data = d
        self.left_size = 0
        self.left, self.right = None, None


    def insert(self, d):
        if d <= self.data:
            if self.left != None:
                self.left.insert(d)
            else:
                self.left = RankedNode(d)
            self.left_size += 1
        elif d > self.data:
            if self.right != None:
                self.right.insert(d)
            else:
                self.right = RankedNode(d)

    def getRank(self,d):
        if d == self.data:
            return self.left_size
        elif d < self.data:
            if self.left == None:
                return -1
            else:
                return self.left.getRank(d)
        else:
            right_size = -1 if self.right == None else self.right.getRank(d)
            if right_size == -1:
                return -1
            return self.left_size + 1 + right_size


def rankFromStream(stream, target):
    root = None
    for num in stream:
        if root is None:
            root = RankedNode(num)
        else:
            root.insert(num)

    return root.getRank(target)

print(rankFromStream([1, 2, 3, 4, 5], 4))

