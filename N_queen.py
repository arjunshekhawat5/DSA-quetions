

# def is_safe(qeen):
#    for i in range(j + 1):
#        if qeens[i][0] == j or qeens[i][1] == row or qeens[i][0]-qeens[i][1] == j - row or qeens[i][0] + qeens[i][1] == j + row:
#            return False
#    return True


def N_queen(n, row):
    # checks if its the end of the grid
    if n == row:
        return True

    # now we check for every cell - (i, row)
    for i in range(n):
        is_safe = True
        # now we check if this cell is safe for every qeen placed previously
        for qeen in qeens:
            if qeen[0] == i or qeen[1] == row or qeen[0]-qeen[1] == i - row or qeen[0] + qeen[1] == i + row:
                is_safe = False
        # if its safe we can place the qeen and go to next iteration of the recursion
        if is_safe:
            qeens.append([i, row])
            if N_queen(n, row + 1):
                return True
            # if we can not go further then we remove the queen placed in this row and check for next cells in the same row
            qeens.pop(-1)
    return False


n = int(input("Enter the size of the grid: "))
qeens = []
if N_queen(n, 0):
    print(qeens)
