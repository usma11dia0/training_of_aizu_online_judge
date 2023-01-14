# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_A&lang=ja

x_1, y_1, x_2, y_2 = map(float, input().split())
distance = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** (1 / 2)
print(distance)
