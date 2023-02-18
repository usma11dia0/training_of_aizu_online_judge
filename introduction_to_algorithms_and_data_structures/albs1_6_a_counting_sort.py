def counting_sort(A: list, k: int) -> list:
    C = [0] * (max(A) + 1)
    # C[i]にAの要素の出現数を記録する。
    for a in A:
        C[a] += 1

    # C[i]にi以下の数の出現数(累積和)を記録する。
    for i in range(1, max(A) + 1):
        C[i] = C[i] + C[i - 1]

    # C[i]を用いてAの後ろからソートしていく。※前からだと重複した数が後ろ側へソートされてしまうため。
    # C[i](累積和)の値 = 配列Aにおいてi以下の要素の数がいくつあるかを示す
    # ⇔ 先頭から数えてその要素が何番目にあるかを示す。
    B = [0] * (k + 1)
    for i in range(k - 1, -1, -1):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
    return B[1:]


n = int(input())
A = list(map(int, input().split()))
print(*counting_sort(A, n))
