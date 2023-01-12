# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_6_C&lang=ja

# 入力情報の取得
n = int(input())
b = [0] * n  # b棟
f = [0] * n  # f階
r = [0] * n  # r番目
v = [0] * n  # v人入居

for i in range(0, n):
    b[i], f[i], r[i], v[i] = map(int, input().split())

# 各棟の配列を生成
house_1 = [[0] * 11 for _ in range(4)]
house_2 = [[0] * 11 for _ in range(4)]
house_3 = [[0] * 11 for _ in range(4)]
house_4 = [[0] * 11 for _ in range(4)]

# 入力情報に基づき配列内に入居者数を追記
for i in range(0, n):
    if b[i] == 1:
        house_1[f[i]][r[i]] += v[i]
    elif b[i] == 2:
        house_2[f[i]][r[i]] += v[i]
    elif b[i] == 3:
        house_3[f[i]][r[i]] += v[i]
    elif b[i] == 4:
        house_4[f[i]][r[i]] += v[i]

# 配列格納
house_all = [house_1, house_2, house_3, house_4]

# 結果の出力
cnt = 0
for house in house_all:
    cnt += 1
    for i in range(1, 4):
        for j in range(1, 11):
            print(f" {house[i][j]}", end="")
        print()
    if cnt != 4:
        print("####################")
