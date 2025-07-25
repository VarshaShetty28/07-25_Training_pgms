# Empty an array (Leetcode - 2659)
def empty_array_steps(arr):
    steps = 0
    while arr:
        smallest = min(arr)  
        if arr[0] == smallest:
            arr.pop(0)
        else:
            arr.append(arr.pop(0))
        steps += 1
    return steps

print(empty_array_steps([5, 5, 5])) 
