# 参考URL
# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=1572340#1


class D_Linked_List:
    class Node:
        def __init__(self, key, next=None, prev=None):
            self.next = next
            self.prev = prev
            self.key = key

    def __init__(self):
        self.nil = D_Linked_List.Node(None)
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, key):
        node_x = D_Linked_List.Node(key, self.nil.next, self.nil)
        self.nil.next.prev = node_x
        self.nil.next = node_x

    def _listSearch(self, key):
        cur_node = self.nil.next
        while (cur_node != self.nil) and (cur_node.key != key):
            cur_node = cur_node.next
        return cur_node

    def _deleteNode(self, node):
        if node == self.nil:
            return None
        node.prev.next = node.next
        node.next.prev = node.prev

    def deleteFirst(self):
        self._deleteNode(self.nil.next)

    def deleteLast(self):
        self._deleteNode(self.nil.prev)

    def deleteKey(self, key):
        node = self._listSearch(key)
        self._deleteNode(node)

    def show_keys(self):
        cur_node = self.nil.next
        keys = []
        while cur_node != self.nil:
            keys.append(str(cur_node.key))
            cur_node = cur_node.next
        print(" ".join(keys))


# 入力データの取得
n = int(input())
command_list = [list(map(str, input().split())) for _ in range(0, n)]

# 初期値の設定
doubly_linked_list = D_Linked_List()

for command in command_list:
    if command[0] == "insert":
        doubly_linked_list.insert(int(command[1]))
    elif command[0] == "delete":
        doubly_linked_list.deleteKey(int(command[1]))
    elif command[0] == "deleteFirst":
        doubly_linked_list.deleteFirst()
    elif command[0] == "deleteLast":
        doubly_linked_list.deleteLast()

doubly_linked_list.show_keys()
