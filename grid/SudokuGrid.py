import math
import CellToFill


class SudokuGrid:
    def __init__(self, fileName):
        file = open("../games/"+fileName, "r")
        data = []
        for x in file:
            data.append(x)

        # create empty sudoku grid
        self.gridSize = int(data[0])
        self.numberOfBlocks = math.sqrt(self.gridSize)
        self.sudoku = [[0]*self.gridSize]*self.gridSize

        # save valid symbols
        self.validSymbols = set()
        symbolsSplit = data[1].split()
        for symbol in symbolsSplit:
            self.validSymbols.add(int(symbol))

        # fill cells according to file input
        for i in (2, len(data)):
            dataSplit = data[i].split()
            rowColumnSplit = dataSplit[0].split(",")
            self.sudoku[rowColumnSplit[0]
                        ][rowColumnSplit[1]] = int(dataSplit[1])

        # prepare empty cells
        self.generateEmptyCells()

    def findCandidates(self, cellToFill):
        row = cellToFill.getRow()
        column = cellToFill.getColumn()
        blockRow = cellToFill.getBlockRow()
        blockColumn = cellToFill.getBlockColumn()

        # remove used symbol in the same row
        symbolsInRow = set(self.sudoku[row])
        symbolsInRow.remove(0)
        candidatesClearRow = self.validSymbols.difference(symbolsInRow)

        # remove used symbol in the same column
        symbolsInColumn = set()
        for rowNumber in self.gridSize:
            if (self.sudoku[rowNumber][column] != 0):
                symbolsInColumn.add(self.sudoku[rowNumber][column])
        candidatesClearRowAndColumn = candidatesClearRow.difference(
            symbolsInColumn)

        # remove used symbol in the same block
        symbolsInBlock = set()
        for blockRow in self.numberOfBlocks:
            for blockColumn in self.numberOfBlocks:
                for row in self.numberOfBlocks:
                    gridRow = row+blockRow*self.numberOfBlocks
                    for column in self.numberOfBlocks:
                        gridColumn = column+blockColumn*self.numberOfBlocks
                        if (self.sudoku[gridRow][gridColumn] != 0):
                            symbolsInBlock.add(
                                self.sudoku[gridRow][gridColumn])
        candidates = candidatesClearRowAndColumn.difference(symbolsInBlock)

        # save candidates in cell
        if (len(candidates) != 0):
            cellToFill.setCandidates(candidates)
            return True
        else:
            return False

    # generate empty cells
    def generateEmptyCells(self):
        self.emptyCells = []
        for blockRow in self.numberOfBlocks:
            for blockColumn in self.numberOfBlocks:
                for row in self.numberOfBlocks:
                    gridRow = row+blockRow*self.numberOfBlocks
                    for column in self.numberOfBlocks:
                        gridColumn = column+blockColumn*self.numberOfBlocks
                        if (self.sudoku[gridRow][gridColumn] == 0):
                            self.emptyCells.append(CellToFill(
                                gridRow, gridColumn, blockRow, blockColumn))

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

    def outputGrid(self, filename):
        return ""

    # getters
    def getEmptyCells(self):
        return self.emptyCells

    def getSudoku(self):
        return self.sudoku

    def getValidSymbols(self):
        return self.validSymbols

    def getGridSize(self):
        return self.gridSize
