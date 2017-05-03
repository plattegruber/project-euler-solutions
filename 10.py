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

def getAllPrimesBelow(n):
    primes = [2, 3]
    currentNum = 3
    while currentNum < n:
        currentNum += 2
        if isprime(currentNum):
            primes.append(currentNum)
    return primes

print(sum(getAllPrimesBelow(2000000)))