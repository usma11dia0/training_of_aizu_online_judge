# 入力データの取得
n = int(input())
R_t = [int(input()) for _ in range(0, n)]

# 初期値の設定
max_price = -(10**10)
min_price = 10**10

for i in range(0, n):
    max_price = max(max_price, R_t[i] - min_price)
    min_price = min(min_price, R_t[i])  # i時点でのmin_priceが確定する点がポイント
print(max_price)
