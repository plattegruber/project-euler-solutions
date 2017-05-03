def isPalendrome(value):
    strValue = str(value)
    return strValue[::-1] == strValue
    
maxValue = 0
i,j = 999, 999
while i > 99:
    while j > 99:
        product = i * j
        if product > maxValue and isPalendrome(product):
            maxValue = product
        j -= 1
    j = 999
    i -= 1

print(maxValue)