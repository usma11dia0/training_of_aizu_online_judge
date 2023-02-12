class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key):
        if not self.head:
            self.head = self.tail = Node(key)
        else:
            self.head = self.head.prev = Node(key, None, self.head)

    def delete(self, key):
        curr = self.head
        while curr:
            if curr.key == key:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                break
            curr = curr.next

    def deleteFirst(self):
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.prev = None

    def deleteLast(self):
        if self.tail:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None


def solve():
    n = int(input().strip())
    dll = DoublyLinkedList()
    for i in range(n):
        op = input().strip().split()
        if op[0] == "insert":
            dll.insert(int(op[1]))
        elif op[0] == "delete":
            dll.delete(int(op[1]))
        elif op[0] == "deleteFirst":
            dll.deleteFirst()
        elif op[0] == "deleteLast":
            dll.deleteLast()
    ans = []
    curr = dll.head
    while curr:
        ans.append(str(curr.key))
        curr = curr.next
    print(" ".join(ans))


if __name__ == "__main__":
    solve()
