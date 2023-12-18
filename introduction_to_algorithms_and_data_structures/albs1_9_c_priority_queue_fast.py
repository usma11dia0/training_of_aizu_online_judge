import sys

# 0-indexedで実装
class MaxHeap():

    # 0-indexed
    def __init__(self) -> None:
        self.heap = []
        
    def _max_heapify(self, A: list, i: int, H: int) -> None:
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
            self._max_heapify(A, largest_index, H)

    def _build_max_heap(self, A: list, H: int) -> None:
        if H > 0:
            for i in range((H - 1) // 2, -1, -1):
                self._max_heapify(A, i, H - 1)
    
    def _insert_upward(self, i: int) -> None:
        A = self.heap
        parent = (i - 1) // 2
        while i > 0 and A[parent] < A[i]:
            A[i], A[parent] = A[parent], A[i]
            i = parent
            parent = (i - 1) // 2
    
    def insert_heap(self, key) -> None:
        self.heap.append(key)
        self._insert_upward(len(self.heap) - 1)
    
    def extract_max(self) -> int:
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap.pop()
        if self.heap:
            self._max_heapify(self.heap, 0, len(self.heap) - 1)
        return data

T = MaxHeap()
output = []

while True:
    command_list = sys.stdin.readline().split()
    if command_list[0] == "insert":
        T.insert_heap(int(command_list[1]))
    elif command_list[0] == "extract":
        result = T.extract_max()
        output.append(str(result))
    elif command_list[0] == "end":
        break

print("\n".join(output))



# 解説
# 二分探索木ではない。(left < root < right)