def romanToInt(s):
    roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    value = [1, 5, 10, 50, 100, 500, 1000]
    dic = {roman[i]: value[i] for i in range(len(value))}

    num = 0
    prev = 0
    s = s[::-1]
    for i in s:
        # check if current number is less then prev value and subtract the value from our num
        if dic[i] < prev:
            num -= dic[i]
            continue
        # track this value for next value's comparision
        else:
            prev = dic[i]
        # add the value of our current roman to our num
        num += dic[i]
    return num


print(romanToInt('XXVII'))
