def merge(A: list, left: int, mid: int, right: int) -> None:
    global cnt
    inf = 10**9 + 1
    L = A[left:mid] + [inf]
    R = A[mid:right] + [inf]

    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        cnt += 1


def merge_sort(A: list, left: int, right: int) -> None:
    if left + 1 < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)


# 入力データの取得
n = int(input())
S = list(map(int, input().split()))

cnt = 0
merge_sort(S, 0, n)
print(*S)
print(cnt)
