class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_front(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next

    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None

    def delete_last(self):
        if self.tail is None:
            return
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.key, end=" ")
            current = current.next
        print()


# Main program
n = int(input())
dll = DoublyLinkedList()
for i in range(n):
    cmd = input().split()
    if cmd[0] == "insert":
        dll.insert_front(int(cmd[1]))
    elif cmd[0] == "delete":
        dll.delete(int(cmd[1]))
    elif cmd[0] == "deleteFirst":
        dll.delete_first()
    elif cmd[0] == "deleteLast":
        dll.delete_last()
dll.print_list()
