




def paintFill(grid, row, column, new_color):
    if grid[row][column] == new_color:
        return False
    return paintFill(grid, row, column, grid[row][column], new_color)



def paintFill(grid, row, column, old_color, new_color):
    if row < 0 or row >= len(grid[0]) or column < 0 or column >= len(grid):
        return False

    if grid[row][column] == old_color:
        grid[row][column] = new_color
        paintFill(grid, row + 1, column, old_color, new_color)
        paintFill(grid, row - 1, column, old_color, new_color)
        paintFill(grid + 1, row, column, old_color, new_color)
        paintFill(grid - 1, row, column, old_color, new_color)
    return True