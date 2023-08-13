from collections import deque

# 入力
n = int(input())
input = [list(map(int, input().split())) for _ in range(n)]

# 隣接リストの作成
# 0-indexed 要素0番目は番兵
adj_list = [list() for i in range(n + 1)]  # adj_list[i] は頂点 i に隣接する頂点のリスト
for row in input:
    # 頂点番号
    u = row[0]
    # 出次数
    k = row[1]
    if k != 0:
        for i in range(0, k):
            t = row[2 + i]
            adj_list[u].append(t)

# 幅優先探索の初期化 (初期化はdist[i] = -1で実施する)
dist = [-1] * (n + 1)  # 答えを格納するリスト
dist[1] = 0  # 頂点1→頂点1の距離は必ず0
Q = deque()  # Qの中に最短距離xの頂点が格納されていく
Q.append(1)  # 下記のループで最初にキューの先頭を削除するため、初期値(頂点1)をキュー内に入れておく

# 幅優先探索
while len(Q) >= 1:
    pos = Q.popleft()  # Qの先頭を削除し、posへ代入
    for nex in adj_list[pos]:  # 頂点posの隣接ノードを一つ一つ調べる
        if dist[nex] == -1:  # 頂点nex(posの隣)の最短距離がまだ記録されていなければ
            dist[nex] = dist[pos] + 1  # posの最短距離+1をnexの最短距離として記録
            Q.append(nex)  # posの最短距離+1の頂点を新たにキュー内へ追加

# 頂点1から各頂点までの最短距離を出力
for i in range(1, n + 1):
    print(f'{i} {dist[i]}')