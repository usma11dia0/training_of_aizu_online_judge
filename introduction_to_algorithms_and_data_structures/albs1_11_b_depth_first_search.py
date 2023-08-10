import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)

# 深さ優先探索を行う関数（pos は現在位置、Gは隣接リスト, visited[x] は頂点 x が青色かどうかを表す真偽値 ）
def dfs(pos, G, visited):  # pos:int, G:list, visited:list
    visited[pos] = True  # 現在位置を青色に塗る(訪問済みにする)
    for i in G[pos]:  # 現在位置の隣接ノード(i)を一つ一つ調べる。後半で再帰呼び出しているため、隣接リストを網羅出来る。
        if visited[i] == False:  # もし隣接ノードが白色(未訪問)だったら、
            dfs(i, G, visited)  # 隣接ノードiを現在位置としてdfsを再帰呼び出し
    # 再帰毎にdfs()のforループの残り(callstack)が溜まっていく
    # for i in G[pos]:のループが終わり次第、dfs()の返り値でNoneが返る
    # Noneが返った後は溜まったcallbackを処理する。 →　本の一つ戻るを表現

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
            adj_list[t].append(u)
print(adj_list) 

# 深さ優先探索
# 0-index 要素0番目は番兵
visited = [False] * (n + 1)
dfs(1, n, visited)

# # print(visited)　※visited[x] は頂点 x が青色かどうかを表す真偽値
# # 出力結果：[False, True, True, True, True, True, True]

# # 連結かどうかの判定（answer = True のとき連結）
# answer = True
# for i in range(1, N + 1):
#     if visited[i] == False:
#         answer = False

# # 答えの出力
# if answer == True:
#     print("The graph is connected.")
# else:
#     print("The graph is not connected.")