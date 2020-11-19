from collections import Counter


def main(arr):
    count = 0
    count_dict = Counter(arr)
    for i in range(len(arr)):
        num = k - arr[i]
        count_dict[arr[i]] -= 1
        for j in count_dict:
            if num - j in count_dict:
                pass
