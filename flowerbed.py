
def canflower_1(fb, n):
    if len(fb) == 0:
        return False
    if (fb[0] == 0 and (n-1) == 0) or n == 0:
        return True
    else:
        return False

    if fb[0] == 0 and fb[1] == 0:
        fb[0] = 1
        n -= 1
    if n == 0:
        return True
    for i in range(1, len(fb) - 2):
        if fb[i] == 0 and fb[i-1] == 0 and fb[i+1] == 0:
            fb[i] = 1
            n -= 1
    if fb[-1] == 0 and fb[-2] == 0:
        fb[-1] = 1
        n -= 1
    if n <= 0:
        return True
    return False


def canflower(fb, n):


}


# !(condition)
print(canflower([0, 0, 0, 0, 1, 0, 1], 1))

'''
 1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1
[0,1,0,1]
[1,0,0,0,0,1]
2
[0,0,1,0,1]
1



if  fb[-2]== 0 and fb[-1] == 0:
    c += 1
'''
