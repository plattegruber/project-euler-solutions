import math

def getNumLatticePaths(size):
    # given by the cominatorics equation found at http://mathworld.wolfram.com/BinomialCoefficient.html
    # and solving where a == b
    return math.factorial(size * 2) // (math.factorial(size) ** 2)
    
    
print(getNumLatticePaths(20))
    