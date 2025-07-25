def first_missing_positive(nums):
    n = len(nums)
    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            correct_index = nums[i] - 1
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


nums = [3, 4, -1, 1]
print(first_missing_positive(nums))  # Output: 2
