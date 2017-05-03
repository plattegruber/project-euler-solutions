def isEven(num):
    return num % 2 == 0
    
def fibonacciGenerator(maxValue):
    #initialize the first two values
    i = 2
    result = [1, 1]
    prev = 1
    
    while i < maxValue:
        result.append(i)
        i, prev = i + prev, i
    
    return result
    
sum = 0
for i in fibonacciGenerator(4000000):
    if isEven(i):
        sum = sum + i
        
print(sum)
        
    