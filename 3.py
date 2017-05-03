def generatePrimeFactors(target):
    factors = []
    d = 2
    while target > 1:
        while target % d == 0:
            factors.append(d)
            target /= d
        d = d + 1
        if d*d > target:
            if target > 1: factors.append(target)
            break
    return factors
    
print(max(generatePrimeFactors(600851475143)))