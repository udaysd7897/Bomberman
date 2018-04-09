import globally
globally.init()


class Clear():
    def clear(row, col):
        globally.matrix[row][col] = ' '
        globally.matrix[row][col + 1] = ' '
        globally.matrix[row][col + 2] = ' '
        globally.matrix[row][col + 3] = ' '
        globally.matrix[row + 1][col] = ' '
        globally.matrix[row + 1][col + 1] = ' '
        globally.matrix[row + 1][col + 2] = ' '
        globally.matrix[row + 1][col + 3] = ' '
