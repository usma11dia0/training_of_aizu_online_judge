# 0-indexedで実装
def max_heapify(A: list, i: int, H: int) -> None:
    left_child_index = 2 * i + 1
    right_child_index = 2 * i + 2
    # 左の子、自分、右の子で値が最大のノードを選ぶ
    if left_child_index <= H and A[left_child_index] > A[i]:
        largest_index = left_child_index
    else:
        largest_index = i
    if right_child_index <= H and A[right_child_index] > A[largest_index]:
        largest_index = right_child_index

    if largest_index != i:
        # A[i]とA[largest]を交換
        A[i], A[largest_index] = A[largest_index], A[i]
        max_heapify(A, largest_index, H)

def buildMaxHeap(A: list, H: int) -> None:
    for i in range((H - 1) // 2, -1, -1):
        max_heapify(A, i, H - 1)

h = int(input())
A = list(map(int, input().split()))

buildMaxHeap(A, h)
output = " ".join(map(str, A))
print(f' {output}')






# 解説 buildMaxHeap(A)にて ループの始点がH/2となっている理由

# 完全二分木には、特定の特性があります。配列におけるインデックス iの要素に対して、その左の子は 2*i インデックスに、右の子は 2*i + 1 インデックスに位置するという特性です。

# したがって、この特性に基づいて考えると、配列の長さ（要素数）を n としたとき、インデックス n/2 の要素以降の要素は、すべて子ノードを持たない葉ノードになります。なぜなら、もし n/2 よりも大きなインデックス i に対して 2*i または 2*i + 1 が存在するとすれば、それは n を超えてしまうからです。したがって、それらのノードは葉ノードであると結論付けられます。

# 例えば、配列の長さが 6（0から数えて6要素）の場合を考えてみましょう：
# 配列：[16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
# インデックス： 0   1   2   3  4  5  6  7  8  9
# ここでインデックス n/2 = 6/2 = 3 以降のインデックス i に対して 2*i または 2*i + 1 を計算すると、それは n を超えてしまいます。したがって、インデックス 3 以降のノードはすべて葉ノードとなります。

# このように、完全二分木の特性を利用することで、配列の半分以上の要素（中間位置以降）が葉ノードであることがわかります。そのため、buildMaxHeap アルゴリズムは、葉ノードでは何もしない maxHeapify を適用する必要がない中間位置から開始することができます。