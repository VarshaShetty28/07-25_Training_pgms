def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return n == sum(d ** 3 for d in digits)

result = []
for i in range(101, 1000):
    if is_armstrong(i):
        result.append(i)

print(result)
