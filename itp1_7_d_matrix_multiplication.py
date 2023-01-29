n, m, l = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(0, n)]
B = [list(map(int, input().split())) for _ in range(0, m)]

C = [[0] * l for _ in range(0, n)]

for i, a_i in enumerate(A):
    # 行列Bを転置して1行ずつ抽出
    for j, b_j in enumerate(zip(*B)):
        C[i][j] = sum(a_i_k * b_k_j for a_i_k, b_k_j in zip(a_i, b_j))

for result in C:
    print(*result)
