triangle = []
with open('problem_files/67.txt', 'r') as f:
    for line in f:
        inner_list = [int(value.strip()) for value in line.split(' ')]
        triangle.append(inner_list)

def getMaxPathForNode(triangle, i, j):
    return triangle[i][j] + max(triangle[i+1][j], triangle[i + 1][j + 1])
    
def getMaxPathForTriangle(triangle):
    for i in range(len(triangle) - 1)[::-1]:
        for j in range(len(triangle[i])):
            triangle[i][j] = getMaxPathForNode(triangle, i, j)
    return triangle[0][0]
    
print(getMaxPathForTriangle(triangle))