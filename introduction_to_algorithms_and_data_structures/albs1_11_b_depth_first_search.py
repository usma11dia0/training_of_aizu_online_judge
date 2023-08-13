import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 深さ優先探索を行う関数
def dfs(pos: int, G: list, visited: list, d: list, f: list, cnt: int) -> int:
    visited[pos] = True  # 現在位置を青色に塗る(訪問済みにする)
    cnt += 1
    d[pos] = cnt
    for i in G[pos]:  # 現在位置の隣接ノード(i)を一つ一つ調べる。
        if visited[i] == False:  # もし隣接ノードが白色(未訪問)だったら、
            cnt = dfs(i, G, visited, d, f, cnt)  # 隣接ノードiを現在位置としてdfsを再帰呼び出し
    cnt += 1
    f[pos] = cnt
    return cnt

# 入力
n = int(input())
input = [list(map(int, input().split())) for _ in range(n)]

# 隣接リストの作成
# 0-indexed 要素0番目は番兵
adj_list = [list() for i in range(n + 1)]  # G[i] は頂点 i に隣接する頂点のリスト
for row in input:
    # 頂点番号
    u = row[0]
    # 出次数
    k = row[1]
    if k != 0:
        for i in range(0, k):
            t = row[2 + i]
            adj_list[u].append(t)
            # adj_list[t].append(u) #反対方向も加えると無効グラフの隣接リストを示す。
print(adj_list) 

# 深さ優先探索
# 0-index 要素0番目は番兵
visited = [False] * (n + 1)
# d[v]: vを最初に発見した時刻
d = [-1] * (n + 1)
# f[v]: vを最後に発見した時刻
f = [-1] * (n + 1)
cnt = 0
dfs(1, adj_list, visited, d, f, cnt)

for i in range(1, n + 1):
    print(f'{i} {d[i]} {f[i]}')