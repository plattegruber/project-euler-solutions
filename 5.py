from collections import defaultdict

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

def countInstances(iterable, target):
    count = 0
    for i in iterable:
        if i == target:
            count += 1
    return count

def getPrimeFactors(numbers):
    # create a dictionary to keep track of powers
    primeFactors = {}
    for number in numbers:
        factors = generatePrimeFactors(number)
        for i in factors:
            totalOccurances = countInstances(factors, i)
            if i in primeFactors: 
                if primeFactors[i] < totalOccurances:
                    primeFactors[i] = totalOccurances
            else:
                primeFactors[i] = totalOccurances
    return primeFactors

def LeastCommonMultiple(numbers):
    # using the prime factorization method found here: https://artofproblemsolving.com/wiki/index.php?title=Least_common_multiple
    primeFactors = getPrimeFactors(numbers)
    product = 1
    for key, value in primeFactors.items():
        product *= key ** value
    return product
    
print(LeastCommonMultiple([x + 1 for x in range(20)]))