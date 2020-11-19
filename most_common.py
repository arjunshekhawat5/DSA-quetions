from collections import Counter


def topKFrequent(nums, k):
    count = Counter(nums)
    count = count.most_common(k)
    ans = []
    for i in count:
        ans.append(i[0])

    count = {}
    for i in nums:
        if i not in count:
            count[i] = 0
        count[i] += 1

    count = sorted(count.items(), key=lambda i: i[1])
    print(count)
    return ans


def main():
    nums = [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 9]
    topKFrequent(nums, 3)


main()
