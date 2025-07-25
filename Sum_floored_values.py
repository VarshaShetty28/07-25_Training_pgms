#Sum of floored values (Leetcode: 1862)
def Sum_Floor_Values(list_num):
    dictionary = {}
    product = 0
    n = len(list_num)
    for i in range(n):
        for j in range(n):
            key = list_num[i]//list_num[j]
            if not key in dictionary:
                dictionary[key]=[]
            dictionary[key].append([list_num[i],list_num[j]])
    print(f"Pairs are: ",dictionary)
    for key,value in dictionary.items():
        product +=key * len(value)
    return product
    
def Sum_Floor_Values_only_val(list_num):
    n = len(list_num)
    product = 0
    for i in range(n):
        for j in range(n):
            product += list_num[i]//list_num[j]
    return product
list_nums=[3,4,2]
print(f"Sum From 1st function: ",Sum_Floor_Values(list_nums))
print(f"Sum From 2nd function: ",Sum_Floor_Values_only_val(list_nums))
