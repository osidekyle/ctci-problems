



class EightQueens:
    def __init__(self):
        self.GRID_SIZE = 8

    def main(self):
        results = []
        cols = [None] * self.GRID_SIZE
        self.placeQueens(0, cols, results)
        return results


    def placeQueens(self, row, cols, results):
        if row == self.GRID_SIZE:
            results.append(cols)
        else:
            for col in range(self.GRID_SIZE):
                if self.checkValid(cols, row, col):
                    cols[row] = col
                    self.placeQueens(row + 1, cols, results)

    def checkValid(self, cols, row1, col1):
        for row2 in range(row1):
            col2 = cols[row2]

            if col1 == col2:
                return False

            columnDistance = abs(col1 - col2)
            rowDistance = row1 - row2

            if columnDistance == rowDistance:
                return False

        return True


print(len(EightQueens().main()))