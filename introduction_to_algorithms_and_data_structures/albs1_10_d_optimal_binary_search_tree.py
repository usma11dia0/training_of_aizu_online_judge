n = int(input())
p = list(map(float, input().split()))
q = list(map(float, input().split()))

# e and w are initialized with 0
e = [[0.0 for _ in range(n+2)] for _ in range(n+2)]
w = [[0.0 for _ in range(n+2)] for _ in range(n+2)]

# Initialize the diagonal elements
for i in range(1, n+2):
    e[i][i-1] = q[i-1]
    w[i][i-1] = q[i-1]

# Calculate e[i][j] and w[i][j]
for l in range(n):
    for i in range(1, n-l+1):
        j = i+l
        e[i][j] = min([e[i][r-1] + e[r+1][j] for r in range(i, j+1)]) + w[i][j]
        w[i][j] = w[i][j-1] + p[j-1] + q[j]

print(e[1][n])