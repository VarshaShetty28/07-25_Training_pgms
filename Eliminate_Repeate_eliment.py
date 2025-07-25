def Eliminate_Repiting(nums):
    if not nums:
        return 0
    pointer = 1
    for i in range(1,len(nums)):
        if nums[i-1] != nums[i]:
            nums[pointer] = nums[i]
            pointer += 1      
    return pointer
        
    

nums = [2,2,4,6,6,8]
ans = Eliminate_Repiting(nums)
print(nums[:ans])  
