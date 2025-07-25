def Repeating_num(num,n):
    actual_total = (n*(n+1))//2
    current_sum = sum(num)
    return current_sum - actual_total

n = 6
nums = [1,2,3,4,4,5,6]   
print(Repeating_num(nums,n)) 
