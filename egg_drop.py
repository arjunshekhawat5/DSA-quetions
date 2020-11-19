def egg_drop(k, n):
    if n == 1 or n == 0:
        return n
    if k == 1:
        return n
    f_min = float("inf")
    for i in range(1, n + 1):
        f = 1 + max([egg_drop(k, n-i), egg_drop(k-1, i-1)])
        f_min = min(f_min, f)
    return f_min


def dynamic_egg_drop(k, n):
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            if i == 1:
                mtr[i][j] = j
                continue
            elif j == 1:
                mtr[i][j] = j
                continue
            mtr[i][j] = float('inf')
            for l in range(1, j+1):
                mtr[i][j] = min(mtr[i][j], 1 + max(mtr[i][j-l], mtr[i-1][l-1]))
    return mtr[k][n]


def egg_drop_opt(k, n):
    if n == 1 or n == 0:
        return n
    if k == 1:
        return n
    if mtr[k][n] != -1:
        return mtr[k][n]
    f_min = float("inf")
    for i in range(1, n + 1):
        if mtr[k][n-i] != -1:
            high = mtr[k][n-i]
        else:
            high = egg_drop_opt(k, n-i)
            mtr[k][n-i] = high

        if mtr[k-1][i-1] != -1:
            low = mtr[k-1][i-1]
        else:
            low = egg_drop_opt(k-1, i-1)
            mtr[k-1][i-1] = low
        f_min = min(f_min, 1 + max(low, high))
    mtr[k][n] = f_min
    return f_min


def egg_drop_opt_2(k, n):
    for i in range(n+1):
        mtr[i][1] = i
    for i in range(k+1):
        mtr[1][k] = 1
    for i in range(2, n+1):
        for j in range(2, k+1):
            mtr[i][j] = float('inf')
            for x in range(1, i):
                low = mtr[x - 1][j - 1]
                high = mtr[i - x][j]
                temp = 1 + max(low, high)
                if temp < mtr[i][j]:
                    mtr[i][j] = temp
    return mtr[-1][-1]


def black_box(egg, floor):
    dp = [[0]*(egg+1) for i in range(floor+1)]
    for i in range(1, floor+1):
        for j in range(1, egg + 1):
            dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
            if dp[i][j] >= floor:
                return i


'''
k = int(input('Enter the number of eggs: '))
n = int(input('Enter the number of floors: '))
mtr = [[0]*(n+1) for _ in range(k+1)]

#print('Min attempts to find the pivotal floor in the worst case', egg_drop(k, n))
'''
k = int(input('Enter the number of eggs: '))
n = int(input('Enter the number of floors: '))
mtr = [[-1]*(k+1) for _ in range(n+1)]


print(egg_drop_opt_2(k, n))
