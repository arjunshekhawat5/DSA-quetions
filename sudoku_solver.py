def breaking(baord, row, col, i):
    # check the current row
    if str(i) in board[row]:
        return True

    # Check every entry in column
    for row_1 in range(len(board)):
        if board[row_1][col] == str(i):
            return True

    # todo check for subgrid placement
    square_x = int(row/3) * 3
    square_y = int(col/3) * 3
    for k in range(square_x, square_x+3):
        for j in range(square_y, square_y+3):
            if board[k][j] == str(i) and k != row and j != col:
                return True
    return False


def next_cell(row, col):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                return i, j
    return False


def solver(board, row, col):
    # base cases
    #tru = next_cell(row, col)
    # if not tru:
    #   return True
    #row, col = tru
    if row >= len(board):
        return True
    elif col == len(board):
        return solver(board, row + 1, 0)
    elif board[row][col] != '.':
        return solver(board, row, col + 1)
    # check for valid placements
    for i in range(1, 10):
        if not breaking(board, row, col, i):
            board[row][col] = str(i)
            if solver(board, row, col+1):
                return True
            board[row][col] = '.'
    return False


board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8',
                                                                                                                                                                                                      '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '.', '4', '1', '9', '.', '.', '5'], ['.', '.', '.', '.', '8', '.', '.', '7', '9']]

col_len = len(board[0])
solver(board, 0, 0)
for i in board:
    print(i)
# if row == len(board):
#        return
#   if col == len(board):
#      solver(board, row+1, 0)
# if board[row][col] != ".":
#    solver(board, row, col+1)
['5', '3', '4', '6', '7', '8', '9', '1', '2']
['6', '7', '2', '1', '9', '5', '3', '4', '8']
['1', '9', '8', '3', '4', '2', '5', '6', '7']
['8', '5', '9', '7', '6', '1', '4', '2', '3']
['4', '2', '6', '8', '5', '3', '7', '9', '1']
['7', '1', '3', '9', '2', '4', '8', '5', '6']
['9', '6', '1', '5', '3', '7', '2', '8', '4']
['2', '8', '7', '4', '1', '9', '6', '3', '5']
['3', '4', '5', '2', '8', '6', '1', '7', '9']

['5', '3', '4', '6', '7', '8', '9', '1', '2']
['6', '7', '2', '1', '9', '5', '3', '4', '8']
['1', '9', '8', '3', '4', '2', '5', '6', '7']
['8', '5', '9', '7', '6', '1', '4', '2', '3']
['4', '2', '6', '8', '5', '3', '7', '9', '1']
['7', '1', '3', '9', '2', '4', '8', '5', '6']
['9', '6', '1', '5', '3', '7', '2', '8', '4']
['2', '8', '7', '4', '1', '9', '6', '3', '5']
['3', '4', '5', '2', '8', '6', '1', '7', '9']
