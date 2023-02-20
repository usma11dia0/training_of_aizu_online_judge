def partition(A: list, p: int, r: int) -> int:
    """
    A[r]との大小を基準に配列Aを分類する。
    A[r]の左側: A[r]よりも小さい要素
    A[r]の右側: A[r]よりも大きい要素

    Parameters
    ----------
    A: list
      分類対象のリスト
    p: int
      始点
    r: int
      終点

    Returns
    -------
    pivot_index: int
      A[r]のindex
    """
    x = A[r]
    # i:境目のpivot_index。i+1にA[r]が入る。
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


n = int(input())
A = list(map(int, input().split()))
pivot_index = partition(A, 0, len(A) - 1)
A[pivot_index] = f"[{A[pivot_index]}]"
print(*A)
