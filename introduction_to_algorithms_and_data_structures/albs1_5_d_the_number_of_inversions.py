from typing import Tuple


def merge_sort(arr: list) -> Tuple[list, int]:
    n = len(arr)
    # 末尾再帰
    if n <= 1:
        return arr, 0
    mid = n // 2
    left_list, cnt_left_list = merge_sort(arr[:mid])
    right_list, cnt_right_list = merge_sort(arr[mid:])
    result = []
    i = j = 0
    cnt = cnt_left_list + cnt_right_list

    # 再帰で得られた左側リストと右側リストの要素の大小を一つずつ比較
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            result.append(left_list[i])
            i += 1

        # 左 > 右の時, 順番の入れ替えが発生。
        else:
            result.append(right_list[j])
            j += 1
            # 反転回数は、左側リストでまだ比較されず残っている要素の数
            cnt += len(left_list) - i
    result += left_list[i:]
    result += right_list[j:]
    return result, cnt


n = int(input())
arr = list(map(int, input().split()))
_, cnt = merge_sort(arr)
print(cnt)
