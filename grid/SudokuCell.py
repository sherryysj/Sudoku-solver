class SudokuCell:
    def __init__(self, row, column, blockRow, blockColumn):
        self.row = row
        self.column = column
        self.blockRow = blockRow
        self.blockColumn = blockColumn
        self.candidate = {}

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getBlockRow(self):
        return self.blockRow

    def getBlockColumn(self):
        return self.blockColumn

    def getCandidate(self):
        return self.candidate
