import math

class PythogoreanTriplet:
    a = 0
    b = 0
    c = 0
    
    def __init__(self, i, j, k):
        self.a = i
        self.b = j
        self.c = k

def generatePythagoreanTriplets():
    i, j = 1, 1
    while i < 10000:
        while j < 10000:
            k = (i ** 2 + j ** 2) ** (1 / 2)
            if k.is_integer():
                yield PythogoreanTriplet(i, j, k)
            j += 1
        j = 1
        i += 1
            
targetSum = 1000
for triplet in generatePythagoreanTriplets():
    if triplet.a + triplet.b + triplet.c == targetSum:
        print(triplet.a * triplet.b * triplet.c)
        break