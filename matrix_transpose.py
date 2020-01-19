"""In this example, you will learn to transpose a matrix (which is created by using a nested list)."""
#defined 3X4 matrix
x = [[12, 3, 4, 5],
     [5, 6, 7, 8],
     [9, 7, 4, 2]]
res = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        #important line below
        res[j][i] = x[i][j]
print(res)