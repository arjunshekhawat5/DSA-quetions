'''
count = 0
max_yet = float('-inf')
nums = [-1, 4, 2, 3]
for i in range(0, len(nums)):
    print(max_yet, count)
    if max_yet < nums[i]:
        max_yet = nums[i]
        continue
    if count == 1:
        print(False)
    max_yet = nums[i]
    count += 1
print(True)


count = 0
max_yet = float('-inf')
for i in range(len(nums) - 1):
    if nums[i] < nums[i+1]:
        continue
    nums.pop(i)
    break
print(nums)
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print False
print True




def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


curr = 0
nums = [-1, 4, 2, 3]
if is_sorted(nums):
    print(True)
for i in range(len(nums) - 1):
    if nums[i] <= nums[i+1]:
        continue
    curr = i
    break

temp = nums[:]
temp.pop(curr)
if is_sorted(temp):
    print(True)
temp = nums[:]
temp.pop(curr+1)
if is_sorted(temp):
    print(True)
else:
    print(False)


test case- [-1,4,2,3]      t
                [3,4,2,3]       f
                [4,2,1]          f
                [4,2,3]          t
                [-1,4,2,1]     f
                [5,7,1,8]       t
                [2,3,3,2,4]     t
'''


def checkPossibility(nums):
    def is_sorted(nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True
    count = 0
    curr = 0
    if is_sorted(nums):
        return True
    for i in range(len(nums) - 1):
        if nums[i] <= nums[i+1]:
            continue
        curr = i
        break
    print(nums)
    temp = nums[:]
    temp.pop(i)
    if is_sorted(temp):
        return True
    temp = nums[:]
    temp.pop(i+1)
    if is_sorted(temp):
        return True
    else:
        return False
