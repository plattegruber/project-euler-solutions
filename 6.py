def sumOfSquares(numbers):
    total = 0
    for number in numbers:
        total += number ** 2
    return total
    
def squareOfSums(numbers):
    return sum(numbers) ** 2
    
values = [x + 1 for x in range(100)]
print(squareOfSums(values) - sumOfSquares(values))