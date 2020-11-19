def permute(space, perm, result):
    if not space:
        result.append(perm)
        return
    for i in range(len(space)):
        temp = space[i]
        temp2 = perm[:]
        perm += [temp]
        permute(space[:i] + space[i+1:], perm, result)
        perm = temp2
    return


def main():
    nums = [1, 2, 3]
    result = []

    print(permute(nums, [], result))
    print(result)
    nums.reverse()
    print(nums)


main()
