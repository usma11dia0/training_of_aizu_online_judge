# 参考：競技プログラミングの鉄則p125 第4章 二次元のDP 最長共通部分列問題

def lcs(S: list, T: list) -> int:
    # 空の配列を準備
    # 0-indexed. 0番目の要素は番兵。
    dp = [[0] * (len(S) + 1) for _ in range(0, len(T) + 1)]
    diagonal = 0
    for i in range(1, len(T) + 1):  # 縦に進む
        for j in range(1, len(S) + 1):  # 横に進む
            if S[j - 1] == T[i - 1]:
                # 斜めに進む (sのi番目とtのj番目が一致していた場合)
                diagonal = dp[i - 1][j - 1] + 1
                dp[i][j] = max(diagonal, dp[i - 1][j], dp[i][j - 1])
            # 斜めに進まない場合 (sのi番目とtのj番目が一致していない場合) max内のdiagonalを除く
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[len(T)][len(S)]

if __name__ == "__main__":
    q = int(input())
    result = []
    for i in range(0, q):
        s = list(input())
        t = list(input())
        result.append(lcs(s, t))
    for r in result:
        print(r)



