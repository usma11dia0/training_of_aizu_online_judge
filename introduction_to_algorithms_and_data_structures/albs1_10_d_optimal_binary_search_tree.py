# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7764500#1

# n: キーの個数
# k: キーk_iは内部節点
# d: ダミーキーd_iは葉をそれぞれ示す。 

n = int(input())
# p[i]: 各キーk_iに対して、探索が起きる確率
p = [0] + list(map(float, input().split()))
# q[i]: 各ダミーキーq_iで、探索が終了する確率 (※内部節点k_iにて探索が生じない確率も含む)
q = list(map(float, input().split()))

# e: 探索コストの期待値を格納する二次元リスト
# e[i][j]: キーk_iからキーk_jの範囲において、最適な二分探索木の探索コストの期待値
# 0-indexed 要素0番目は番兵
e = [[0]*(n + 1) for _ in range(n + 1)]

# w: 確率の合計を格納する二次元リスト
# w[i][j]: キーk_iからキーk_jまで、およびそれに隣接するダミーキーの確率の合計値
# 　　　　　≒その範囲内で探索が終了する確率の合計。範囲iからjの最適な二分探索木の探索コストに一様に影響
#          → p[i]～p[j]の合計 + q[i-1]～q[j]の合計
w = [[0]*(n + 1) for _ in range(n + 1)]

# 探索範囲がキーk_iからキーk_iになる時
# 探索はダミーキーd_iで終了 (探索が発生していないためp[i]は無し)
for i in range(n + 1):
    # 探索コストの期待値e = q_i
    e[i][i] = q[i]
    # 確率の合計はq_iのみ
    w[i][i] = q[i]

# 探索範囲を1～nまで順に変化させてループ
# 例えばl = 2の時は、2つのキーに対する最適な二分探索木を求める。
for l in range(1, n + 1):
    # 与えられた探索範囲の幅 lに対して、全ての可能な始点 iをループ 
    # 例えばn = 5, l = 2の時, i = 0, 1, 2の3通り
    # (※iには内部節点kだけでなくダミーキーd含むため、0も始点に含む)
    for i in range(0, n - l + 1):
        # 終点 jは 始点 i + 探索範囲 l 
        j = i + l
        # k_i～k_j及びそれに隣接するダミーキーの確率の合計は、
        # k_i～k_j-1の確率合計にk_jの探索が発生した確率とd_jで探索が終了した確率を足したもの
        w[i][j] = w[i][j-1] + p[j] + q[j]
        
        # 範囲iからjの中で最適な二分探索木のルートとするキーrを選ぶ。
        # → 範囲iからjの中でルートとして選ばれる各キーに対して、左部分木のコストe[i][r-1]と右部分木のコストe[r+1][j]の和を計算。
        # その最小値を選択
        e[i][j] = min(e[i][r] + e[r+1][j] for r in range(i, j))
        
        # w[i][j]は、範囲iからjまでの全てのキーとダミーキーに対する探索確率の合計
        # このコストは、どのキーがルートとして選ばれるかによらず、部分木全体の探索コストに一様に加えられる
        e[i][j] += w[i][j]

print(e[0][n])



# 具体例
# n = 3 （内部節点の数）
# p = [0, 0.4, 0.3, 0.3] （各キーが探索の対象となる確率）
# q = [0.1, 0.1, 0.1, 0.1] （各ダミーキーが探索の対象となる確率）
# 処理の流れ
# l = 1の場合： 1つのキーに対する最適な二分探索木を求めます。

# i = 0, j = 1: この範囲にはキーk_1のみがあります。
# w[0][1] = w[0][0] + p[1] + q[1] = 0.1 + 0.4 + 0.1 = 0.6
# e[0][1] = min(e[0][0] + e[1][1]) + w[0][1] = 0.1 + 0.1 + 0.6 = 0.8
# 同様に、他のiの値でも計算します。
# l = 2の場合： 2つのキーに対する最適な二分探索木を求めます。

# i = 0, j = 2: この範囲にはキーk_1とk_2があります。
# w[0][2] = w[0][1] + p[2] + q[2] = 0.6 + 0.3 + 0.1 = 1.0
# e[0][2] = min(e[0][0] + e[1][2], e[0][1] + e[2][2]) + w[0][2] = min(0.1 + 0.4, 0.8 + 0.1) + 1.0 = 1.3
# 同様に、他のiの値でも計算します。
# l = 3の場合： 3つのキーに対する最適な二分探索木を求めます。

# i = 0, j = 3: この範囲にはキーk_1、k_2、k_3があります。
# w[0][3] = w[0][2] + p[3] + q[3] = 1.0 + 0.3 + 0.1 = 1.4
# e[0][3] = min(e[0][0] + e[1][3], e[0][1] + e[2][3], e[0][2] + e[3][3]) + w[0][3]
# この計算は、異なるルートとして選べるキー（k_1、k_2、k_3）それぞれに対して行います。
# 最終結果はe[0][3]に格納され、これが全体の期待値を最小にする二分探索木の探索コストの期待値となります。


