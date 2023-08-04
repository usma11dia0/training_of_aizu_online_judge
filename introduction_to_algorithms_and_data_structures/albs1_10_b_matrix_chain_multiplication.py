# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1196722#1
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=8018761#1

# https://qiita.com/ikamirin/items/5ddbe04cb4d4ce6ed6af

n = int(input())
data =[list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

# 一番左の行列の行数, 各行列の列数の配列で連鎖行列(M_1～M_i)を示す。
# 例：(3,2), (2,3), (3,1)　→　[3,2,3,1]で表すことができる。
# data = [[30, 35], [35, 15]....]
matrices = [data[0][0]] + [d[1] for d in data]

# 動的計画法で短い連鎖行列積の値を保持しながら計算していく。
# 連鎖行列長2からnまでループ開始 (連鎖行列長1は調べる必要なし)
for length in range(2, n + 1):
    # 連鎖行列長に対し、開始位置(i)と終了位置(j)を決めて対象範囲をスライド
    # 開始位置の範囲は1から n - length + 1 まで
    # 例：ABCDの4つの連鎖行列を長さ2がスライドする場合、長さ分を引いて引いたあとの次のインデックスの3が最大開始位置になる
    for i in range(1, n - length + 2):
        # 終了位置(j): 開始位置に長さ分を足し、1を引いたインデックス
        j = i + length - 1
        dp[i][j] = float("inf")
        for k in range(i, j):
            tmp = dp[i][k] + dp[k + 1][j] + matrices[i - 1] * matrices[k] * matrices[j]
            dp[i][j] = min(dp[i][j], tmp)
print(dp[1][n])