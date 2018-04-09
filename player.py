from position import Position
from wall import *
from movement import Movement
from clear import Clear


class Player(Position):
    def __init__(self, x, y, lives):
        Position.__init__(self, x, y)
        self.lives = lives

    def deployplayer(self):
        globally.matrix[self.x][self.y] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x][self.y + 1] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x][self.y + 2] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x][self.y + 3] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x + 1][self.y] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x + 1][self.y + 1] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x + 1][self.y + 2] = '\u001b[0;32mB\u001b[0m'
        globally.matrix[self.x + 1][self.y + 3] = '\u001b[0;32mB\u001b[0m'

    def getrow(self):
        return self.x

    def getcol(self):
        return self.y

# if player is killed by bomb
    def bombkill(self):
        self.lives -= 1
        Movement.move('\u001b[0;33me\u001b[0m', self.x, self.y)
        self.x = 2
        self.y = 4
        Player.deployplayer(self)

# if player is killed by bomb
    def enemykill(self):
        self.lives -= 1
        Movement.move('\u001b[0;31mE\u001b[0m', self.x, self.y)
        self.x = 2
        self.y = 4
        Player.deployplayer(self)

    def mvright(self):
        if (globally.matrix[self.x][self.y + 4] == ' '):
            self.y += 4
            Movement.move('\u001b[0;32mB\u001b[0m', self.x, self.y)
            if (globally.matrix[self.x][self.y - 4] == '\u001b[0;32mB\u001b[0m'):
                Clear.clear(self.x, self.y - 4)

    def mvleft(self):
        if (globally.matrix[self.x][self.y - 4] == ' '):
            self.y -= 4
            Movement.move('\u001b[0;32mB\u001b[0m', self.x, self.y)
            if (globally.matrix[self.x][self.y + 4] == '\u001b[0;32mB\u001b[0m'):
                Clear.clear(self.x, self.y + 4)

    def mvdown(self):
        if (globally.matrix[self.x + 2][self.y] == ' '):
            self.x += 2
            Movement.move('\u001b[0;32mB\u001b[0m', self.x, self.y)
            if (globally.matrix[self.x - 2][self.y] == '\u001b[0;32mB\u001b[0m'):
                Clear.clear(self.x - 2, self.y)

    def mvup(self):
        if (globally.matrix[self.x - 2][self.y] == ' '):
            self.x -= 2
            Movement.move('\u001b[0;32mB\u001b[0m', self.x, self.y)
            if (globally.matrix[self.x + 2][self.y] == '\u001b[0;32mB\u001b[0m'):
                Clear.clear(self.x + 2, self.y)
