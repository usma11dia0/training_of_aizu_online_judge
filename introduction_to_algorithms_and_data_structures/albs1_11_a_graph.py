n = int(input())
# 0-indexed
adj_matrix = [[0] * n for _ in range(n)]

for _ in range(n):
    line = list(map(int, input().split()))
    # 頂点番号
    u = line[0] - 1
    # 出次数
    k = line[1]
    for i in range(0, k):
        v = line[2 + i] - 1
        adj_matrix[u][v] = 1

for row in adj_matrix:
    print(*row)