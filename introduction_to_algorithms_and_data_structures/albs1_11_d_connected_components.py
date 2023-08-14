class UnionFind:
    # n頂点の Union-Find 木を作成
    def __init__(self, n):  # nには頂点の数Nが入る。
        self.n = n
        self.par = [-1] * (n + 1)  # parは親を示す。-1は全ての頂点に親がいないことを示す。
        self.size = [1] * (n + 1)  # sizeはグループの頂点数。初期値は各グループ頂点1つのため1。

    # 頂点xの根を返す
    def root(self, x):
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 要素u, vを含むグループを統合
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        if root_u != root_v:
            # uとvが異なるグループのときのみ処理を行う
            # Union By Sizeによる場合分け。頂点数の多いグループの根を上に持っていく
            if self.size[root_u] < self.size[root_v]:
                self.par[root_u] = root_v
                self.size[root_v] += self.size[root_u]
            else:
                self.par[root_v] = root_u
                self.size[root_u] += self.size[root_v]

    #  要素uとvが同一のグループかどうかを判定
    def same(self, u, v):
        return self.root(u) == self.root(v)

# 入力
n, m = map(int, input().split())
uf = UnionFind(n)
output = []

for i in range(0, m):
    s, t = map(int, input().split())
    uf.unite(s, t)

q = int(input())
for j in range(0, q):
    s, t = map(int, input().split())
    if uf.same(s, t):
        output.append('yes')
    else:
        output.append('no')

print('\n'.join(output))