def paren(count, perm, res):
    if count[")"] == 0 or count["("] == 0:
        if count["("] == 0:
            for i in range(count[")"]):
                perm += ")"
        temp = perm[:]
        # if perm not in res:
        res.append(perm)
        return
    total = count['('] + count[')']

    temp = perm[:]
    if count["("] < count[")"] and count[')'] != 0:
        perm += ")"
        count[")"] -= 1
        paren(count, perm, res)
        perm = temp
        count[")"] += 1
    if count['('] != 0:
        perm += "("
        count["("] -= 1
        paren(count, perm, res)
        count["("] += 1
        perm = temp


def main():
    n = 8
    count = {
        '(': n,
        ')': n
    }
    res = []
    paren(count, "", res)
    print(res)


main()
