import sys


class Node:
    def __init__(self, key: int, next_node=None, prev_node=None) -> None:
        self.key = key
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.pnt = Node(None)
        # pnt.next = head
        self.pnt.next = self.pnt
        # pnt.prev = tail
        self.pnt.prev = self.pnt

    # 先頭にキーxを持つ要素を継ぎ足す
    def insert(self, key: int) -> None:
        # キーxのノードを生成
        # ノードを生成した時点でnode.nextに現HEAD, node.prevにNone(Node)を入れる)
        new_node = Node(key, self.pnt.next, self.pnt)

        if self.pnt.next is None:  # リストが空の場合
            self.pnt.prev = new_node

        self.pnt.next.prev = new_node
        self.pnt.next = new_node

    def _deleteNode(self, node):
        if node == self.pnt:
            return None
        # node.prev ⇔ node ⇔　node.next から
        # node.prev ⇔ node.next
        node.prev.next = node.next
        node.next.prev = node.prev

    # キーxを持つ最初のノードを連結リストから削除する。そのような要素が存在しない場合は何もしない。
    def delete(self, key: int) -> None:
        current_node = self.pnt.next

        # キーxを持つノード(current_node)を抽出
        while current_node.key and current_node.key != key:
            current_node = current_node.next
        self._deleteNode(current_node)

    # 連結リストの先頭の要素を削除する
    def deleteFirst(self) -> None:
        self._deleteNode(self.pnt.next)

    # 連結リストの末尾の要素を削除する
    def deleteLast(self) -> None:
        self._deleteNode(self.pnt.prev)

    # 連結リストのキーを出力する
    def print_key(self) -> None:
        current_node = self.pnt.next
        while current_node.key:
            if current_node.next.key == None:
                print(current_node.key)
            else:
                print(current_node.key, end=" ")
            current_node = current_node.next


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

doubly_linked_list.print_key()

# doubly_linked_list = DoublyLinkedList()

# for i in sys.stdin:
#     if "insert" in i:
#         x = i[7:-1]
#         doubly_linked_list.insert(x)
#     elif "deleteFirst" in i:
#         doubly_linked_list.deleteFirst()
#     elif "deleteLast" in i:
#         doubly_linked_list.deleteLast()
#     elif "delete" in i:
#         x = i[7:-1]
#         doubly_linked_list.delete(x)
#     else:
#         pass

# doubly_linked_list.print_key()
