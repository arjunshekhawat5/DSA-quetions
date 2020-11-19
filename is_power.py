'''
Given an integer Richard and louise plays a game where they take turn on number as if number is a power of 2,
player divides the number by 2 and gives the number to the other player and if number if not power of 2 player gives the remainder to other player
if the number recieved by the player is 1 he loses. Determines who wins the game given the integer and louise takes first turn.
'''


def is_power(n):
    pow = 1
    x = 2
    while x <= n:
        if x == n:
            return True, pow
        x = x**2
        pow *= 2
    lo, hi = pow//2, pow
    while lo < hi:
        mid = (lo+hi)//2
        if 2**mid == n:
            return True, mid
        elif 2**mid < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return False, n - 2**(lo - 1)


print(is_power(132))


def counterGame(n):
    score = 1
    if n == 1:
        return 'Richard'
    while n > 1:
        ans = is_power(n)
        print(ans)
        if ans[0] == True:
            score *= (-1)**(ans[1] - 1)
            break
        else:
            n = ans[1]
            score *= -1
    if score == 1:
        return 'Richard'
    else:
        return 'Lousie'


print(counterGame(128))
