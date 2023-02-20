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
    x = int(A[r][1])
    i = p - 1
    for j in range(p, r):
        if int(A[j][1]) <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quick_sort(A: list, p: int, r: int) -> list:
    """
    配列Aを昇順にソートする。

    Parameters
    ----------
    A: list
     ソート対象のリスト
    p: int
     始点
    r: int
     終点

    Returns
    -------
    None
    """
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


def is_stable(A: list, B: list, n: int) -> bool:
    """
    配列Aが安定ソートかどうかを判定する。

    Parameters
    ----------
    A: list
     ソート済みのリスト
    B: list
     ソート前のリスト
    n: int
     リストの要素数

    Returns
    -------
    is_stable: bool
     安定:True
     不安定:False
    """
    A_dict = {}
    B_dict = {}
    for i in range(0, n):
        A_dict.setdefault(A[i][1], []).append(A[i][0])
        B_dict.setdefault(B[i][1], []).append(B[i][0])
    if A_dict == B_dict:
        is_stable = True
    else:
        is_stable = False
    return is_stable


n = int(input())
card_list = [list(map(str, input().split())) for _ in range(0, n)]
card_list_sorted = card_list.copy()
quick_sort(card_list_sorted, 0, len(card_list) - 1)

if is_stable(card_list_sorted, card_list, n):
    print("Stable")
else:
    print("Not stable")

for card in card_list_sorted:
    print(*card)
