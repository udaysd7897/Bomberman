from wall import *
from random import *


# To print bricks on board
class Bricks():
    for i in range(20):
        row, col = 0, 0
        while(globally.matrix[row][col] != ' '):
            row = randint(2, 35)
            col = randint(4, 75)
        dr = row % 2
        dc = col % 4
        globally.matrix[row - dr][col - dc] = '/'
        globally.matrix[row - dr][col - dc + 1] = '/'
        globally.matrix[row - dr][col - dc + 2] = '/'
        globally.matrix[row - dr][col - dc + 3] = '/'
        globally.matrix[row - dr + 1][col - dc] = '/'
        globally.matrix[row - dr + 1][col - dc + 1] = '/'
        globally.matrix[row - dr + 1][col - dc + 2] = '/'
        globally.matrix[row - dr + 1][col - dc + 3] = '/'
