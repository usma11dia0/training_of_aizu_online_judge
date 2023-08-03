# 0-indexedで実装
def max_heapify(A: list, i: int, h: int) -> None:
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    # 左の子、自分、右の子で値が最大のノードを選ぶ
    if left_child_index <= h and A[left_child_index] > A[i]:
        largest_index = left_child_index
    else:
        largest_index = i
    if right_child_index <= h and A[right_child_index] > A[largest_index]:
        largest_index = right_child_index

    if largest_index != i:
        # A[i]とA[largest]を交換
        A[i], A[largest_index] = A[largest_index], A[i]
        max_heapify(A, largest_index, h)

def build_max_heap(A: list, h: int) -> None:
    if h > 0:
        for i in range((h - 1) // 2, -1, -1):
            max_heapify(A, i, h)

def heap_sort(A: list):
    last_heap_index = len(A) - 1
    build_max_heap(A, last_heap_index)
    while last_heap_index >= 1:
        A[0], A[last_heap_index] = A[last_heap_index], A[0]
        last_heap_index -= 1
        max_heapify(A, 0, last_heap_index)

N = int(input())
A = list(map(int, input().split()))

# 配列Aを昇順にソート
# heap_sort(A)
A.sort()

# 要素番号0(最小値)以外の要素が最大ヒープを満たすよう親と子を入れ替える。
for i in range(1, N - 1):
    # while文から抜ける最後のループの時、A[i]とA[1]の入れ替えが発生するため
    # 先に逆の入れ替えを実施しておく。
    A[0], A[i] = A[i], A[0]

    # 各要素の親と子を入れ替え
    # 昇順にソートされているため、入れ替え後は必ず 親 > 子 (最大ヒープ)が満たされる。
    while i != 0:
        A[i], A[(i - 1)// 2] = A[(i - 1) // 2], A[i]
        i = (i - 1) // 2

#最後に要素番号0(最小値)とN-1(最大値)を入れ替え
A[0], A[N - 1] = A[N - 1], A[0]

print(*A)
