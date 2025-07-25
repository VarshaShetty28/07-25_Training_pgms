def Reverse_string(given_str):
    new_list =given_str.split()
    print(new_list)
    final_list = []
    print(len(new_list))
    for i in range(len(new_list)-1,-1,-1):
        print(i)
        # print(new_list[i])
        final_list.append(new_list[i])
    return " ".join(final_list)
    
given_str = "Hello World i!"
ans = Reverse_string(given_str)
print(ans) 
