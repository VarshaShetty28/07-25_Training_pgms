def singlesum(nums):
    new_nums = list(str(nums))
    sum = 0
    for i in new_nums:
        sum += int(i)
        if len(str(sum)) > 1:
            sum = sum % 10 + sum // 10
    return sum


num = 154
val =singlesum(num)
print(val)
