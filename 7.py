def isprime(n):
    n = abs(int(n))

    if n < 2:
        return False

    if n == 2: 
        return True    

    if not n & 1: 
        return False

    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False

    return True

def nthPrime(n):
    count = 2
    currentNum = 3
    while count < n:
        currentNum += 2
        if isprime(currentNum):
            count += 1
    return currentNum

print(nthPrime(10001))