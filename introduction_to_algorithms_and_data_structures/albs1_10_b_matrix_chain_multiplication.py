# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1196722#1
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=8018761#1

# https://qiita.com/ikamirin/items/5ddbe04cb4d4ce6ed6af

n = int(input())
data =[list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

matrices = [data[0][0]] + [d[1] for d in data]

for length in range(2, n + 1):
    for i in range(1, n - length + 2):
        j = i + length - 1
        dp[i][j] = float("inf")
        for k in range(i, j):
            tmp = dp[i][k] + dp[k + 1][j] + matrices[i - 1] * matrices[k] * matrices[j]
            dp[i][j] = min(dp[i][j], tmp)
print(dp[1][n])