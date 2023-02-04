# 入力データの取得
n = int(input())
A_list = list(map(int, input().split()))
q = int(input())
m_list = list(map(int, input().split()))

for m in m_list:

    # dp[i][j] : 0,1,2...iまでのAの要素を足し合わせ、jを作る事が出来ればTrue,
    # 　　　　　　そうでなければFalseを返す。
    dp = [[0] * (m + 1) for _ in range(0, n + 1)]

    # 初期値を設定
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(0, m + 1):
            # "－"のインデックスによる配列参照対策
            if j - A_list[i - 1] < 0:
                if dp[i - 1][j] == True:
                    dp[i][j] = True
            if j - A_list[i - 1] >= 0:
                # dp[i][j]がTrueになるための条件
                # 1. i-1の時点ですでにjである時: dp[i-1][j] == True
                # 2. i-1の時点で、あとA[i]を足し合わせればjになる時: dp[i-1][j-A_list[i-1]] = True
                if (dp[i - 1][j] == True) or (dp[i - 1][j - A_list[i - 1]] == True):
                    dp[i][j] = True

    # 結果の出力
    if dp[n][m]:
        print("yes")
    else:
        print("no")
