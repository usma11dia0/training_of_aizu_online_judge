# r:行　c:列
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(0, r)]

# 二次元配列を生成
result_matrix = [[0] * (c + 1) for _ in range(r + 1)]

for i in range(0, r):
    for j in range(0, c):
        # 元の行列
        result_matrix[i][j] = matrix[i][j]
        # 行方向の累積和
        result_matrix[i][c] += matrix[i][j]
        # 列方向の累積和
        result_matrix[r][j] += matrix[i][j]
        # 行と列の累積和
        result_matrix[r][c] += matrix[i][j]

for result in result_matrix:
    print(*result)
