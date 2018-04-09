from wall import *
from random import *
from movement import Movement
from clear import Clear
from position import Position


class Enemy(Position):
    def __init__(self, x, y, direction):
        Position.__init__(self, x, y)
        self.direction = direction

    def deployenemy(self):
        for i in range(2):
                for j in range(4):
                    globally.matrix[self.x + i][self.y + j] = '\u001b[0;31mE\u001b[0m'

    def getrow(self):
        return self.x

    def getcol(self):
        return self.y

    def kill(self):
        Movement.move('\u001b[0;33me\u001b[0m', self.x, self.y)

    def pkill(self):
        Movement.move(' ', self.x, self.y)

# To move enemy in fixed direction
    def mv(self):
        if self.direction == 1:
            if globally.matrix[self.x][self.y + 4] == ' ' or globally.matrix[self.x][self.y + 4] == '\u001b[0;32mB\u001b[0m' or globally.matrix[self.x][self.y + 4] == '\u001b[0;36m0\u001b[0m':
                self.y += 4
                Movement.move('\u001b[0;31mE\u001b[0m', self.x, self.y)
                Clear.clear(self.x, self.y - 4)
            else:
                Enemy.rmv(self)
        elif self.direction == 2:
            if globally.matrix[self.x][self.y - 4] == ' ' or globally.matrix[self.x][self.y - 4] == '\u001b[0;32mB\u001b[0m' or globally.matrix[self.x][self.y - 4] == '\u001b[0;36m0\u001b[0m':
                self.y -= 4
                Movement.move('\u001b[0;31mE\u001b[0m', self.x, self.y)
                Clear.clear(self.x, self.y + 4)
            else:
                Enemy.rmv(self)
        elif self.direction == 3:
            if globally.matrix[self.x - 2][self.y] == ' ' or globally.matrix[self.x - 2][self.y] == '\u001b[0;32mB\u001b[0m' or globally.matrix[self.x - 2][self.y] == '\u001b[0;36m0\u001b[0m':
                self.x -= 2
                Movement.move('\u001b[0;31mE\u001b[0m', self.x, self.y)
                Clear.clear(self.x + 2, self.y)
            else:
                Enemy.rmv(self)
        else:
            if globally.matrix[self.x + 2][self.y] == ' ' or globally.matrix[self.x + 2][self.y] == '\u001b[0;32mB\u001b[0m' or globally.matrix[self.x + 2][self.y] == '\u001b[0;36m0\u001b[0m':
                self.x += 2
                Movement.move('\u001b[0;31mE\u001b[0m', self.x, self.y)
                Clear.clear(self.x - 2, self.y)
            else:
                Enemy.rmv(self)

# To chose direction
    def rmv(self):
        d = randint(1, 4)
        if d == 1:
            if globally.matrix[self.x][self.y + 4] == ' ' or globally.matrix[self.x][self.y + 4] == '\u001b[0;32mB\u001b[0m':
                self.direction = 1
                Enemy.mv(self)
            elif globally.matrix[self.x][self.y - 4] == ' ' or globally.matrix[self.x][self.y - 4] == '\u001b[0;32mB\u001b[0m':
                self.direction = 2
                Enemy.mv(self)
            elif globally.matrix[self.x][self.y - 4] == ' ' or globally.matrix[self.x][self.y - 4] == '\u001b[0;32mB\u001b[0m':
                self.direction = 3
                Enemy.mv(self)
            elif globally.matrix[self.x + 2][self.y] == ' ' or globally.matrix[self.x + 2][self.y] == '\u001b[0;32mB\u001b[0m':
                self.direction = 4
                Enemy.mv(self)
        if d == 2:
            if globally.matrix[self.x][self.y - 4] == ' ' or globally.matrix[self.x][self.y - 4] == '\u001b[0;32mB\u001b[0m':
                self.direction = 2
                Enemy.mv(self)
            else:
                Enemy.rmv(self)
        if d == 3:
            if globally.matrix[self.x - 2][self.y] == ' ' or globally.matrix[self.x - 2][self.y] == '\u001b[0;32mB\u001b[0m':
                self.direction = 3
                Enemy.mv(self)
            else:
                Enemy.rmv(self)
        if d == 4:
            if globally.matrix[self.x + 2][self.y] == ' ' or globally.matrix[self.x + 2][self.y] == '\u001b[0;32mB\u001b[0m':
                self.direction = 4
                Enemy.mv(self)
            else:
                Enemy.rmv(self)
