class Node:
    def __init__(self, key: int, prev_node=None, next_node=None) -> None:
        self.key = key
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    # 先頭にキーxを持つ要素を継ぎ足す
    def insert(self, key: int) -> None:
        # キーxのノードを生成
        new_node = Node(key)
        if self.head == None:
            self.head = new_node
            return
        #  HEAD(old) ⇔ next_node から
        #  HEAD(new_node) ⇔ HEAD(old)  へと変更
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    # キーxを持つ最初のノードを連結リストから削除する。そのような要素が存在しない場合は何もしない。
    def delete(self, key: int) -> None:
        current_node = self.head
        # キーxを持つノードを抽出(=current_node)し、ループを抜ける
        while current_node and current_node.key != key:
            current_node = current_node.next
        if current_node == None:
            return
        # current_nodeが真ん中にある時
        # prev_node ⇔ current_node ⇔ next_node から
        # prev_node ⇔ next_node　へと変更
        else:
            next_node = current_node.next
            prev_node = current_node.prev
            prev_node.next = next_node
            next_node.prev = prev_node
            current_node = None
            return

    # 連結リストの先頭の要素を削除する
    def deleteFirst(self) -> None:
        current_node = self.head
        if current_node:
            # current_nodeしかない場合
            if current_node.next == None:
                current_node = None
                self.head = None
                return
            else:
                #  current_nodeの他にもノードがある場合
                #  HEAD(current_node) ⇔ next_node から
                #  HEAD(next_node) へと変更
                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

    # 連結リストの末尾の要素を削除する
    def deleteLast(self) -> None:
        current_node = self.head
        # 末尾のノードを抽出(=current_node)し、ループを抜ける
        while current_node:
            current_node = current_node.next
        # current_nodeが末尾にある時
        # prev_node ⇔ current_node ⇔ None から
        # prev_node ⇔ None　へと変更
        prev_node = current_node.prev
        prev_node.next = None
        current_node = None

    # 連結リストのキーを出力する
    def print_key(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node.key)
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
