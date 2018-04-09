import globally
globally.init()


class Movement():
    def move(ch, row, col):
        globally.matrix[row][col] = ch
        globally.matrix[row][col + 1] = ch
        globally.matrix[row][col + 2] = ch
        globally.matrix[row][col + 3] = ch
        globally.matrix[row + 1][col] = ch
        globally.matrix[row + 1][col + 1] = ch
        globally.matrix[row + 1][col + 2] = ch
        globally.matrix[row + 1][col + 3] = ch
