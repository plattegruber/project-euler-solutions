import math

def generateTriangularNumbers():
    i = 0
    j = 1
    while True:
        i = i + j
        j += 1
        yield i
        
def getFactors(n):
    factors = []
    sqrtN = math.floor(math.sqrt(n))
    for i in [x + 1 for x in range(sqrtN)]:
        if n % i == 0:
            factors.append(i)
            if i != sqrtN:
                factors.append(n // i)
    factors.append(n)
    return factors

for triangle in generateTriangularNumbers():
    factors = getFactors(triangle)
    if len(factors) > 500:
        print(triangle)
        break