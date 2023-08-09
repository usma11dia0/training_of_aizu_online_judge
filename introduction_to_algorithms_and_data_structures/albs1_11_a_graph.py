# 各頂点に対して隣接リストを読み込む
# 0-indexed
def output_graph(abj_matrix:list) -> int:
    for _ in range(n):
        line = list(map(int, input().strip().split()))
        u = line[0] - 1 # 頂点番号 (0-indexedに変換)
        k = line[1] # u の出次数
        adjacent_vertices = line[2:] # u に隣接する頂点のリスト

        # 隣接行列を更新
        for v in adjacent_vertices:
            adj_matrix[u][v - 1] = 1 # 頂点番号は 0-indexed のため、v - 1 を使用

    # 隣接行列を出力
    for row in adj_matrix:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    n = int(input().strip())
    adj_matrix = [[0] * n for _ in range(n)]

    
