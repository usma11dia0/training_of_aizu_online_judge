# 参考資料 https://www.youtube.com/watch?v=6D7BoKrq7hA&t=9s 45分近辺

# クラスカルのアルゴリズム：どの辺も選択していない状態からスタートし、重みが小さい辺から順番に追加していって最終的に全域木を作る方法 (貪欲法)
# ※ただし閉路となる場合は追加しない(木の定理を満たさないため)

# 各辺を追加する際にunion-findの判定を用いて、かつ条件を満たしたものをunion-findの木に追加することで、クラスカルのアルゴリズムを実装。

# 教訓
# unite()を実装するために必要なこと
# １．頂点aのrootと頂点bのrootを調べる。
# ２．頂点aのルートに紐づくノードの数と頂点bのルートに紐づくノードの数を調べる(Union by Size)
# ３．頂点aのルートと頂点bのルートを連結し新たな木を作成する。その際、新たな木のサイズも更新する。
#     ※※頂点a,bのノード数ではなく、頂点a,bのルートのノード数である点に要注意。

#  list.sort() メソッドには引数にkeyを指定することが可能で、比較を行う前にリストの各要素に対して呼び出される関数を指定出来る

# Union-find木を定義
class UnionFind:
    # 初期化
    def __init__(self, n: int) -> None:
        self.n = n  # Union-Find木の頂点の数
        self.par = [-1] * (n + 1)  # 各頂点の親は初期状態では自分自身(親が自分自身≒親無しの場合-1) ※1-indexedで実装
        self.size = [1] * (n + 1)  # 各頂点に紐づくノードの数は、初期状態では1 ※1-indexedで実装

    # 頂点xのrootを調べる関数
    def root(self, x: int) -> int:
        while self.par[x] != -1:
            x = self.par[x]
        return x

    # 頂点uと頂点vを連結させる関数
    def unite(self, u: int, v: int) -> None:
        # 頂点uとvのrootを調べ、rootが既に同一でないかどうかを調べる。
        rootu = self.root(u)
        rootv = self.root(v)
        # rootが同一でない場合のみ処理を実行
        if rootu != rootv:
            # ノード数が多い頂点を新たなルートにする
            if self.size[rootu] < self.size[rootv]:  # 頂点uよりも頂点vの方がノード数が多い場合
                self.par[rootu] = rootv  # 頂点uのルートの上に、新たなルート(頂点vのルート)を設定
                self.size[rootv] += self.size[rootu]  # 連結された新たな木(頂点vのルート)のサイズを更新する。
            else:
                self.par[rootv] = rootu  # 頂点vのルートの上に、新たなルート(頂点uのルート)を設定
                self.size[rootu] += self.size[rootv]  # 連結された新たな木(頂点uのルート)のサイズを更新する。

    # 頂点uと頂点vが同じ連結成分に属するかどうかを調べる関数
    def same(self, u: int, v: int) -> bool:
        return self.root(u) == self.root(v)


# 入力データの取得
n = int(input())
edges = []
cnt = 0

# 隣接行列より隣接リストを作成
while cnt < n:
    a_i = list(map(int, input().split()))
    for j in range(cnt + 1, n):
        if a_i[j] != -1:
            edges.append([cnt + 1, j + 1, a_i[j]])
    cnt += 1

# 辺(x[2])を長さの小さい順にsortする。
edges.sort(key=lambda x: x[2])  # 比較を行う前にリストの各要素に対して呼び出される関数を指定。
# リストの各要素xとして、x[2]を指定している。

# 最小全域木を求める
uf = UnionFind(n)
answer = 0
for a, b, c in edges:
    if not uf.same(a, b):  # 頂点a,bがまだ同じ連結成分に属していない場合
        uf.unite(a, b)
        answer += c
print(answer)