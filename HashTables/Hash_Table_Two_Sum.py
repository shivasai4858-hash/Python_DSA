
def two_sum(nums, target):
    num_map = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
        print(num_map)
    return []


print(two_sum([5, 1, 7, 2, 9, 3], 10))  
print(two_sum([4, 2, 11, 7, 6, 3], 9))






"""def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums)-1,0,-1):
            if nums[i] + nums[j] == target:
                return [i ,j]
print(two_sum([4, 2, 11, 7, 6, 3], 9)) """