from sys import stdin, maxsize
from typing import List

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
A = [maxsize] + A

def max_heapify(A, index, heap_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    if left_child_index <= heap_size and A[left_child_index] > A[index]:
        largest = left_child_index
    else:
        largest = index
    if right_child_index <= heap_size and A[right_child_index] > A[largest]:
        largest = right_child_index

    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest, heap_size)

def heap_sort(A: List[int], N: int):
    heap_size = N

    for i in range(N // 2, 0, -1):
        max_heapify(A, i, N)

    while heap_size >= 2:
        A[1], A[heap_size] = A[heap_size], A[1]
        heap_size -= 1
        max_heapify(A, 1, heap_size)

# 配列Aを昇順にソート
heap_sort(A, N)
print(f'heap_sort:{A}')

# 要素番号1(最小値)以外の要素が最大ヒープを満たすよう親と子を入れ替える。
for i in range(2, N):
    # while文から抜ける最後のループの時、A[i]とA[1]の入れ替えが発生するため
    # 先に逆の入れ替えを実施しておく。
    A[1], A[i] = A[i], A[1]
    print(A)

    # 各要素の親と子を入れ替え
    # 昇順にソートされているため、入れ替え後は必ず 親 > 子 (最大ヒープ)が満たされる。
    while i != 1:
        # iが子, i//2は親。
        A[i], A[i // 2] = A[i // 2], A[i]
        i = i // 2
        print(A)

#最後に要素番号1(最小値)とN(最大値)を入れ替え
A[1], A[N] = A[N], A[1]

# Print the sorted array (end result)
print(*A[1:])