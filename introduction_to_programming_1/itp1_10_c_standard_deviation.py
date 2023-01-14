# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_C&lang=ja

ans_list = []
while True:
    n = int(input())
    if n == 0:
        break
    s_list = list(map(float, input().split()))

    # 平均の導出
    mean = sum(s_list) / len(s_list)

    # 分散の導出
    sum_var = 0
    for s in s_list:
        sum_var += (s - mean) ** 2
    variance = sum_var / len(s_list)

    # 標準偏差の導出
    std_dev = (variance) ** (1 / 2)
    ans_list.append(std_dev)

for ans in ans_list:
  print(ans)
