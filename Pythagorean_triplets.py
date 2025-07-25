def pythagorean(n_nums):
    val = []
    nums = list(map(abs, n_nums)) 
    nums.sort()
    for i in range(0,len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[k]**2 == nums[i]**2 + nums[j]**2:
                    val.append((nums[i], nums[j], nums[k]))
    return val
                

    

nums = [-5,-3,-4,13,12]
ans =pythagorean(nums)
print(ans)
