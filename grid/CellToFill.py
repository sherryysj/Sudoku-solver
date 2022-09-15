class CellToFill:
    def __init__(self, row, column, blockRow, blockColumn):
        self.row = row
        self.column = column
        self.blockRow = blockRow
        self.blockColumn = blockColumn
        self.candidate = set()

    def getRow(self):
        return self.row

    def getColumn(self):
        return self.column

    def getBlockRow(self):
        return self.blockRow

    def getBlockColumn(self):
        return self.blockColumn

    def setCandidate(self, candidate):
        self.candidate = candidate

    def getCandidate(self):
        return self.candidate
