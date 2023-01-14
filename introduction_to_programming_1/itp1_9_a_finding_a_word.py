# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_A&lang=ja

W = str(input())

ans = 0
while True:
    T = str(input())
    if T == "END_OF_TEXT":
        break

    # Tを大文字で統一
    T_upper = T.upper()
    W_upper = W.upper()

    T_upper_list = T_upper.split()
    for word in T_upper_list:
        if word == W_upper:
            ans += 1
print(ans)
