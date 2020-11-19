# arjun
from collections import Counter
nums = [1, 2, 3]
ans = []

count = Counter(nums)
print(count.most_common(3))


# swap
def subs(nums):
    l = len(nums)
    res = [[]] * (2 ** l)    #
    for i in range(len(res)):
        for j in range(len(nums) + 1):
            count = j
            for k in range(count):
                res[i].append(nums[j])

    print(res)


def subsets(n, porn, nums):

    if n == len(nums):
        return ans.append(perm)

    subsets(n+1, pem, nums)
    subsets(n+1, perm + [nums[n]], nums)


def main():
    perm = []
    subsets(0, perm, nums)
    # subs(nums)


main()
print(ans)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(li, i):
            if i >= len(nums):
                self.res.append(li[:])
                return

            dfs(li + [nums[i]], i + 1)
            dfs(li, i+1)
        dfs([], 0)
        return self.res
