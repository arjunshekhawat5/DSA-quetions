from collections import Counter


def main():
    strr = 'aabb'
    print(func(strr))


def sub_count1(strr):
    counter = 0

    for i in range(len(strr)):
        pass

    return counter


def sub_count(strr):
    sub_palindrome = set()  # to store unique palindrome sequences

    for i in range(len(strr)):
        # finding odd length of palindromes around i
        find_palindrome(strr, i, i, sub_palindrome)

        # finding even lenght of palindromes around i
        find_palindrome(strr, i, i + 1, sub_palindrome)

    print(sub_palindrome, len(sub_palindrome))


def find_palindrome(strr, start, end, sub):

    # we will go in both direction as long as a palindrome is maintained
    while start >= 0 and end < len(strr) and strr[start] == strr[end]:
        # add the palindrome to the set to keep track of unique palindromes
        sub.add(strr[start:end+1])
        start -= 1
        end += 1


def func(string):
    n = len(string)
    count = 0
    for i in range(n):
        odd = {}
        even = {}
        for j in range(i, n):
            if string[j] in odd:
                even[string[j]] = 1
                del odd[string[j]]
            else:
                odd[string[j]] = 1

            if len(odd) < 2:
                count += 1

    return count


main()
