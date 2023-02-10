# 参考URL
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1572340#1

# from __future__ import annotations
import sys


class Node:
    def __init__(self, key: int, next_node=None, prev_node=None) -> None:
        self.key = key
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = head
        self.body = Node(None)
        self.body.next = self.body
        self.body.prev = self.body

    # 先頭にキーxを持つ要素を継ぎ足す
    def insert(self, key: int) -> None:
        # キーxのノードを生成
        new_node = Node(key, self.body.next, self.body)
        self.body.next.prev = new_node
        self.body.next = new_node

    # キーxを持つ最初のノードを連結リストから削除する。そのような要素が存在しない場合は何もしない。
    def delete(self, key: int) -> None:
        current_node = self.body.next

        # キーxを持つノード(current_node)を抽出
        while current_node and current_node.key != key:
            current_node = current_node.next
        if current_node is None:
            return None

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev

    # 連結リストの先頭の要素を削除する
    def deleteFirst(self) -> None:
        self._deleteNode(self.body.next)

        current_node = self.head
        if current_node:
            # current_nodeしかない場合
            if current_node.next == None:
                current_node = None
                self.head = None
                return
            #  current_nodeの他にもノードがある場合
            #  HEAD(current_node) ⇔ next_node から
            #  HEAD(next_node) へと変更
            else:
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

    # 連結リストの末尾の要素を削除する
    def deleteLast(self) -> None:
        current_node = self.head
        # 　要素がHEADのみの場合
        if current_node.next == None:
            current_node = None
            self.head = None
            return

        #  prev_node  ⇔ current_node ⇔ self.tail から
        #  prev_node ⇔ self.tail へと変更
        else:
            current_node = self.tail
            self.tail = current_node.prev
            current_node.prev.next = None
            current_node = None

    # 連結リストのキーを出力する
    def print_key(self) -> None:
        current_node = self.head
        while current_node:
            if current_node.next == None:
                print(current_node.key)
            else:
                print(current_node.key, end=" ")
            current_node = current_node.next


# 入力データの取得
# n = int(input())
# command_list = [list(map(str, input().split())) for _ in range(0, n)]

# # 初期値の設定
# doubly_linked_list = DoublyLinkedList()

# for command in command_list:
#     if command[0] == "insert":
#         doubly_linked_list.insert(int(command[1]))
#     elif command[0] == "delete":
#         doubly_linked_list.delete(int(command[1]))
#     elif command[0] == "deleteFirst":
#         doubly_linked_list.deleteFirst()
#     elif command[0] == "deleteLast":
#         doubly_linked_list.deleteLast()

doubly_linked_list = DoublyLinkedList()

for i in sys.stdin:
    if "insert" in i:
        x = i[7:-1]
        doubly_linked_list.insert(x)
    elif "deleteFirst" in i:
        doubly_linked_list.deleteFirst()
    elif "deleteLast" in i:
        doubly_linked_list.deleteLast()
    elif "delete" in i:
        x = i[7:-1]
        doubly_linked_list.delete(x)
    else:
        pass

doubly_linked_list.print_key()
