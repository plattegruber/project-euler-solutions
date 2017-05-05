def getCollatzChainLength(startingNumber):
    n = startingNumber
    chainLength = 1
    while n > 1:
        if (n % 2 == 0):
            n /= 2
        else:
            n = 3 * n + 1
        chainLength += 1
    return(chainLength)
    
longestValue = 0
longestChain = 0
print('starting...')
for i in range(1, 1000001):
    if i // 100000 > 0 and i % 100000 == 0:
        print(str(i // 10000) + '% done')
    currentChainLength = getCollatzChainLength(i)
    if currentChainLength > longestChain:
        longestChain = currentChainLength
        longestValue = i

print(longestValue)