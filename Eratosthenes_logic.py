def Eratosthenes_prime(num):
    primes = []
    for i in range(2, num+1):
        primes.append(i)
    print(primes)
    for i in range(2, int(num**0.5) + 1):
        remove_elements = []
        for j in primes:
            if j!=i and j%i==0:
                remove_elements.append(j)
        for m in remove_elements:
            primes.remove(m)
    return primes

ans = Eratosthenes_prime(30)
print(ans)
