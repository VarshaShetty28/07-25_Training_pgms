def reverse_number(num):
    is_negative = num < 0
    num = abs(num)
    
    rev_num = 0
    while num > 0:
        rem = num % 10
        rev_num = rev_num * 10 + rem
        num = num // 10

    return -rev_num if is_negative else rev_num

num = 154
print(reverse_number(num))
