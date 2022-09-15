class SudokuGrid:
    def __init__(self, fileName):
        file = open("../games/"+fileName, "r")
        data = []
        for x in file:
            data.append(x)

        # create empty sudoku grid
        self.gridSize = int(data[0])
        self.sudoku = [[0]*self.gridSize]*self.gridSize

        # save valid symbols
        validSymbols = set()
        symbolsSplit = data[1].split()
        for symbol in symbolsSplit:
            validSymbols.add(int(symbol))

        # fill cells according to file input
        for i in (2, len(data)):
            dataSplit = data[i].split()
            rowColumnSplit = dataSplit[0].split(",")
            self.sudoku[rowColumnSplit[0]
                        ][rowColumnSplit[1]] = int(dataSplit[1])

    def outputGrid(self, filename):
        return ""

    # convert sudoku grid to string
    def toString(self):
        columnEndIndex = len(self.sudokuSize) - 1

        sudokuString = ""
        for row in self.sudoku:
            for column in row:
                sudokuString += self.sudoku[row, column]
                if (column < columnEndIndex):
                    sudokuString += " "
            sudokuString += "\n"

        return sudokuString

    def validate(self):
        return ""
