import globally
globally.init()


class Wall():
    globally.matrix = [['\u001b[0;47mX\u001b[0m' for row in range(0, 76)]for col in range(0, 38)]
    for i in range(0, 38):
        for j in range(4, 72):
            if i % 4 == 2 or i % 4 == 3:
                globally.matrix[i][j] = ' '

    for i in range(2, 36):
        for j in range(0, 76):
            if j % 8 == 4 or j % 8 == 5 or j % 8 == 6 or j % 8 == 7:
                globally.matrix[i][j] = ' '
