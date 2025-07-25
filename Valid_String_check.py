# Valid String check (Leetcode - 1003)
def Valid_String_Check(string):
    new_list = []
    for i in string:
        new_list.append(i)
        if new_list[-3:] == ['a','b','c']:
            new_list = new_list[:-3]
    if new_list == []:
        print("Valid")
    else:
        print("Invalid")
strings1 = ['a','a','b','c','b','c'] 
strings2 = ['a','b','c','a','b','c','a','b','c'] 
strings3 = ['a','b','c','c','b','a'] 
Valid_String_Check(strings1)
Valid_String_Check(strings2)
Valid_String_Check(strings3)
