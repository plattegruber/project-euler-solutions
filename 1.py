maxValue = 1000
sum = 0
for i in range(maxValue):
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
print(sum)