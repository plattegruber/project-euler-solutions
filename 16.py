def getPowerDigitSum(base, power):
    result = base ** power
    return sum([x for x in map(int, list(str(result)))])
    
print(getPowerDigitSum(2, 1000))