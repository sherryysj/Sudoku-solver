class BackTracking:
    def __init__(self):
        pass

    def solve(self, grid):
        grid.generateEmptyCells()
        emptyCells = grid.getEmptyCells()
        sudoku = grid.getSudoku()
        validSymbols = grid.getValidSymbols()
        gridSize = grid.getGridSize()

        isSolved = False

        return isSolved
