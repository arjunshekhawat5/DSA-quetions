def findUnsortedSubarray(nums):
    left = 0
    right = len(nums) - 1
    is_sorted = True
    for i in range(len(nums)-1):
        if nums[i] > nums[i + 1]:
            is_sorted = False
            break
    if is_sorted:
        return 0

    while left < right:
        if nums[left] > nums[left+1]:
            break
        left += 1
    while right > 1:
        if nums[right] < nums[right - 1]:
            break
        right -= 1

    max_sort = max(nums[left:right + 1])
    min_sort = min(nums[left: right + 1])
    len_sort = right - left + 1

    for i in range(0, left):
        if nums[i] > min_sort:
            len_sort += left - i
            break
    for i in range(len(nums)-1, right, -1):
        if nums[i] < max_sort:
            len_sort += i - right
            break
    return len_sort


def shortest_unsorted(self, nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1
    sorted_nums = sorted(nums)
    for i in range(len(nums)):
        if nums[i] != sorted_nums[i]:
            left = i
            break
    if i == len(nums) - 1:
        return 0

    for i in range(len(nums)-1, -1, -1):
        if nums[i] != sorted_nums[i]:
            right = i
            break
    return right - left + 1
