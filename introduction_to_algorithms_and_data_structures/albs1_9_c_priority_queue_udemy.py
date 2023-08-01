import sys

class MiniHeap():

    def __init__(self) -> None:
        # 0番目の要素は無限大の負の値とする
        self.heap = [-1 * sys.maxsize]
        self.current_size = 0
    
    def parent_index(self, index: int) -> int:
        return index // 2
    
    def left_child_index(self, index: int) -> int:
        return index * 2
    
    def right_child_index(self, index: int) -> int:
        return index * 2 + 1
    
    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_up(self, index: int) -> None:
        while self.parent_index(index) > 0:
            if self.heap[index] < self.heap[self.parent_index(index)]:
                self.swap(index, self.parent_index(index))
            index = self.parent_index(index)

    def min_child(self, index: int) -> int:
        if (self.heap[self.left_child_index(index)] <
            self.heap[self.right_child_index(index)]):
            return self.left_child_index(index)
        else:
            return self.right_child_index(index)

    def heapify_down(self, index: int) -> None:
        while self.left_child_index(index) <= self.current_size:
            self.min_child(index)



    def push(self, value: int) -> None:
        self.heap.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)

    def pop(self) -> int:
        # 要素が一つのみ(index番号0番(無限大の負の値)のみの時)
        if len(self.heap) == 1:
            return
        
        root = self.heap[1]
        data = self.heap.pop()
        if len(self.heap) == 1:
            return root
        
        self.heap[1] = data
        self.current_size -= 1
        self.heapify_down(1)



        return root
    


if __name__ == "__main__":
    min_heap = MiniHeap()
    min_heap.push(5)
    min_heap.push(6)
    min_heap.push(2)
    print(min_heap.heap)

