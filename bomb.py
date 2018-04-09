from player import *
from clear import Clear
import globally
globally.init()


class Bomb(Position):
    def __init__(self, x, y):
        Position.__init__(self, x, y)

    def plant(self):
        for i in range(2):
            for j in range(4):
                globally.matrix[self.x + i][self.y + j] = '\u001b[0;36m2\u001b[0m'

    def getrow(self):
        return (self.x)

    def getcol(self):
        return (self.y)

    def explode(self):
        Bomb.print(self.x, self.y)
        if(globally.matrix[self.x][self.y - 4] != '\u001b[0;47mX\u001b[0m'):
            Bomb.print(self.x, self.y - 4)
        if(globally.matrix[self.x][self.y + 4] != '\u001b[0;47mX\u001b[0m'):
            Bomb.print(self.x, self.y + 4)
        if(globally.matrix[self.x - 2][self.y] != '\u001b[0;47mX\u001b[0m'):
            Bomb.print(self.x - 2, self.y)
        if(globally.matrix[self.x + 2][self.y] != '\u001b[0;47mX\u001b[0m'):
            Bomb.print(self.x + 2, self.y)

    def print(row, column):
        for i in range(2):
            for j in range(4):
                globally.matrix[row + i][column + j] = '\u001b[0;33me\u001b[0m'

    def flame(self):
        Clear.clear(self.x, self.y)
        if(globally.matrix[self.x][self.y - 4] == '\u001b[0;33me\u001b[0m'):
            Clear.clear(self.x, self.y - 4)
        if(globally.matrix[self.x][self.y + 4] == '\u001b[0;33me\u001b[0m'):
            Clear.clear(self.x, self.y + 4)
        if(globally.matrix[self.x - 2][self.y] == '\u001b[0;33me\u001b[0m'):
            Clear.clear(self.x - 2, self.y)
        if(globally.matrix[self.x + 2][self.y] == '\u001b[0;33me\u001b[0m'):
            Clear.clear(self.x + 2, self.y)
