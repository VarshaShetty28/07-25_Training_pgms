def Armstrong_number(num):
    sum_digits = 0
    list_num = list(str(num))
    # print(list_num)
    power = len(list_num)
    for digit in list_num:
        sum_digits+=int(digit)**power
    if sum_digits == num:
        print("Armstrong number")
    else:
        print("Not a Armstrong number")
    
num = int(input("Enter number : "))
Armstrong_number(num)
