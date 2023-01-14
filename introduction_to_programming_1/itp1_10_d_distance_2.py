# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_D&lang=ja

# 関数定義
def cal_distance_2(x: list, y: list, p: int) -> float:
    D_xy = 0
    sum_tmp = 0
    for i in range(0, n):
        sum_tmp += (abs(x_vector[i] - y_vector[i])) ** p
    D_xy = (sum_tmp) ** (1 / p)
    return D_xy


def cal_distance_2_inf(x: list, y: list) -> float:
    D_xy = 0
    for i in range(0, n):
        tmp = abs(x_vector[i] - y_vector[i])
        D_xy = max(D_xy, tmp)
    return D_xy


# 入力データの取得
n = int(input())
x_vector = list(map(float, input().split()))
y_vector = list(map(float, input().split()))

# 結果の出力(p=1～3)
for p in range(1, 4):
    print(cal_distance_2(x_vector, y_vector, p))

# 結果の出力(p=∞)
print(cal_distance_2_inf(x_vector, y_vector))
