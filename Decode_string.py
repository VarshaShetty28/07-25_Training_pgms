def decode_string(s):
    stack = []
    curr_str = ""
    num = 0

    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '[':
            stack.append((curr_str, num))
            curr_str = ""
            num = 0
        elif char == ']':
            prev_str, times = stack.pop()
            curr_str = prev_str + curr_str * times
        else:
            curr_str += char

    return curr_str


s = "3[a]2[bc]"
result = decode_string(s)
print(result)
