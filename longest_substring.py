string=input("Enter the string: ")
def LongestSub(string):
    current_sub=[]
    longest_sub=[]
    for ch in string:
        if ch in current_sub:
            index=current_sub.index(ch)
            current_sub=current_sub[index+1:]
        current_sub.append(ch)
            
        if len(current_sub)>len(longest_sub):
            longest_sub=current_sub[:]
                
    return ''.join(longest_sub)

print(LongestSub(string))
