from wall import *
from player import Player
from bricks import Bricks
from bomb import Bomb
from enemy import Enemy
from movement import Movement
from random import *
import sys
import os
# p is the instance of Player class
p = Player(2, 4, 3)
p.deployplayer()

# array 'en' is an array of enemies
en = []
count = 3
# count = number of enemies

# For deploying enemies
for i in range(count):
    row, col = 0, 0
    while(globally.matrix[row][col] != ' ' and globally.matrix[row][col] != '\u001b[0;32mB\u001b[0m'):
        row = randint(2, 35)
        col = randint(4, 75)
        direction = i + 1
        row -= row % 2
        col -= col % 4
    e = Enemy(row, col, direction)
    e.deployenemy()
    en.append(e)
fb = 0

# For printing board
for i in range(0, 38):
    for j in range(0, 76):
        print(globally.matrix[i][j], end = '')
    print("")
ch = '1'

while(ch != 'q'):
    # To input character from terminal
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd,  termios.TCSADRAIN,  old_settings)
# Player movement
    if ch == 'd':
        p.mvright()
    if ch == 's':
        p.mvdown()
    if ch == 'a':
        p.mvleft()
    if ch == 'w':
        p.mvup()

# enemy movement
    for i in range(count):
        en[i].mv()
        if(en[i].getrow() == p.getrow() and en[i].getcol() == p.getcol()):
            p.enemykill()

# plant bomb
    if ch == 'b':
        if fb == 0:
            fb = 1
            b = Bomb(p.getrow(), p.getcol())
            b.plant()
# bx,by coordinate of bomb
            bx = b.getrow()
            by = b.getcol()
    if(fb != 0):
        fb += 1
# bomb variation frmae by frame
        if(fb == 2):
            Movement.move('\u001b[0;36m2\u001b[0m', bx, by)
        if(fb == 3):
            Movement.move('\u001b[0;36m1\u001b[0m', bx, by)
        if(fb == 4):
            Movement.move('\u001b[0;36m0\u001b[0m', bx, by)
# wall destruction
        if(fb == 5):
            if(globally.matrix[bx][by - 4] == '/'):
                globally.score += 20

            if(globally.matrix[bx][by + 4] == '/'):
                globally.score += 20

            if(globally.matrix[bx - 2][by] == '/'):
                globally.score += 20

            if(globally.matrix[bx + 2][by] == '/'):
                globally.score += 20
# bomb explosion
            b.explode()
# px,py coordinate of player
            px = p.getrow()
            py = p.getcol()
# killing player by bomb
            if(bx == px):
                if(by == py - 4 or by == py + 4):
                    p.bombkill()
            if(by == py):
                if(px == bx - 2 or px == bx + 2):
                    p.bombkill()
# killing enemy by bomb
# ex,ey coordinatte of each player
            for i in range(count):
                ex = en[i].getrow()
                ey = en[i].getcol()
                if(bx == ex):
                    if(by == ey - 4 or by == ey + 4 or by == ey):
                        en[i].kill()
                        globally.score += 100
                        en.pop(i)
                        count -= 1
                        break
                if(by == ey):
                    if(bx == ex - 2 or bx == ex + 2 or bx == ex):
                        en[i].kill()
                        globally.score += 100
                        en.pop(i)
                        count -= 1
                        break
        if(fb == 6):
            b.flame()
            fb = 0
# entities to be displayed
    os.system('clear')
    for i in range(0, 38):
        for j in range(0, 76):
            print (globally.matrix[i][j], end = '')
        print("")
    print("score :", end = ' ')
    print(globally.score)
    print("lives :", end = ' ')
    print(p.lives)
    if(p.lives == 0):
        print("GAME OVER")
        sys.exit()
