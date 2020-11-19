def main():
    arr = [9, 5, 4, 9]
    b = 3
    sub_ar1(arr, b)


def sub_arr(arr, b):
    count = 0
    for i in range(len(arr)):
        sub_ar = []
        len_sub = 0
        sum_sub = 0
        for j in range(i, b):
            sum_sub += arr[j]
            if arr[j] % b == 0 or len(sub_ar) + 1 > (b-1) or sum_sub % b == 0:
                break
            sub_ar += [arr[j]]
            count += 1
            print(sub_ar, count)


def sub_ar1(arr, b):
    count = 0
    for i in range(len(arr)):
        curr_seq = []
        curr_sum = 0
        curr_len = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            curr_len += 1
            curr_seq += [arr[j]]
            if arr[j] % b == 0 or curr_sum % b == 0:
                print(curr_seq, count, curr_sum, curr_len)
                break
            if curr_len == b-1:
                count += 1
                print(curr_seq, count, curr_sum, curr_len)
                # 1264789
                # 1247
                # 1279
    print(count)


main()
