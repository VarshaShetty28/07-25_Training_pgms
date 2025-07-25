number=int(input("Enter the number: "))
num_list=[]
for i in range(2,number+1):
    num_list.append(i)
for i in range(int((number+1)**0.5)+1):
    j = i + 1
    while j < len(num_list):
        if num_list[j] % num_list[i] == 0:
            num_list.pop(j)  
        else:
            j += 1
twin_pair=[]
for i in range(len(num_list)-1):
    if num_list[i+1]-num_list[i]==2:
        twin_pair.append((num_list[i], num_list[i+1]))
print(twin_pair)
