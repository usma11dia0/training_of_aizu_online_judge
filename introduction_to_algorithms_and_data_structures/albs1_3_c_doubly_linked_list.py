class Node:
    def __init__(self, key: int, prev=None, next=None) -> None:
        self.key = key
        self.prev_node = prev
        self.next_node = next


class DoublyLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    # 先頭にキーxを持つ要素を継ぎ足す
    def insert(self, key: int) -> None:
        new_node = Node(key)
        if self.head == None:
            self.head = new_node
            return
        else:
            current_head_node = self.head
            self.head = new_node
            self.head.next_node = current_head_node

            return

    # キーxを持つ最初の要素を連結リストから削除する。そのような要素が存在しない場合は何もしない。
    def delete(self, key: int) -> None:
        # 連結リストの中からキーxを持つ要素を抽出。
        # 先頭のノードから検索
        current_node = self.head
        while current_node:
            if current_node.key == key:
                break
            current_node = current_node.next_node
        if current_node == None:
            return
        # 抽出したキーxを持つ要素を削除する
        # キーxを持つ要素が先頭にある場合
        self.head = current_node.next_node
        current_node.next_node.prev_node = None
        # キーxを持つ要素が中間にある場合
        current_node.prev_node.next_node = current_node.next_node.prev_node
        # キーxを持つ要素が末尾にある場合
        current_node.prev_node.next_node = None

    # 連結リストの先頭の要素を削除する
    def deleteFirst(self) -> None:
        if self.head == None:
            return
        else:
            self.head = self.head.next_node
            self.head.next_node.prev_node = None

    # 連結リストの末尾の要素を削除する
    def deleteLast(self) -> None:
        if self.head == None:
            return
        current_node = self.head
        while current_node:
            current_node = current_node.next_node
        current_node.prev_node.next_node = None


# 入力データの取得
n = int(input())
command_list = [list(map(str, input().split())) for _ in range(0, n)]

# 初期値の設定
doubly_linked_list = DoublyLinkedList()

for command in command_list:
    if command[0] == "insert":
        doubly_linked_list.insert(int(command[1]))
    elif command[0] == "delete":
        doubly_linked_list.delete(int(command[1]))
    elif command[0] == "deleteFirst":
        doubly_linked_list.deleteFirst()
    elif command[0] == "deleteLast":
        doubly_linked_list.deleteLast()

print(doubly_linked_list.head.key)
print(doubly_linked_list.head.next_node.key)
print(doubly_linked_list.head.next_node.next_node.key)
