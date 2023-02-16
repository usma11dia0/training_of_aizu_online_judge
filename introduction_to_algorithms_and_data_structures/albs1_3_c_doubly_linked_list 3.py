import sys


class Node:
    def __init__(self, key: int, next_node=None, prev_node=None) -> None:
        self.key = key
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self) -> None:

        # リストの先頭(sentinel.next:head)と末尾(sentinel.prev:tail)の
        #  両方を表すダミーノードの作成
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    # 先頭にキーxを持つ要素を継ぎ足す
    def insert(self, key: int) -> None:
        # キーxのノードを生成
        new_node = Node(key, self.sentinel.next, self.sentinel)

        # リストが空の場合
        # 末端(self.sentinel.prev)にnew_nodeを入れる。
        if self.sentinel.next is None:
            self.sentinel.prev = new_node

        # self.sentinel ⇔ self.sentinel.next から
        # self.sentinel ⇔ new_node ⇔ self.sentinel.next へ
        self.sentinel.next.prev = new_node
        self.sentinel.next = new_node

    def _deleteNode(self, node):
        if node == self.sentinel:
            return None
        # node.prev ⇔ node ⇔　node.next から
        # node.prev ⇔ node.next へ
        node.prev.next = node.next
        node.next.prev = node.prev

    # キーxを持つ最初のノードを連結リストから削除する。そのような要素が存在しない場合は何もしない。
    def delete(self, key: int) -> None:
        current_node = self.sentinel.next

        # キーxを持つノード(current_node)を抽出
        while current_node.key and current_node.key != key:
            current_node = current_node.next
        self._deleteNode(current_node)

    # 連結リストの先頭の要素を削除する
    def deleteFirst(self) -> None:
        self._deleteNode(self.sentinel.next)

    # 連結リストの末尾の要素を削除する
    def deleteLast(self) -> None:
        self._deleteNode(self.sentinel.prev)

    # 連結リストのキーを出力する
    def print_key(self) -> None:
        current_node = self.sentinel.next
        while current_node.key:
            if current_node.next.key == None:
                print(current_node.key)
            else:
                print(current_node.key, end=" ")
            current_node = current_node.next


# # 入力データの取得
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

# doubly_linked_list.print_key()


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


# 以下解説-------------------------------------------------------------------------------------------

# このコードは、双方向連結リストを表す DoublyLinkedList クラスを定義し、与えられたコマンドに応じて双方向連結リストを操作するプログラムです。各コマンドの内容は以下の通りです。

# insert x : 双方向連結リストの先頭に、キーが x であるノードを追加する。
# delete x : キーが x である最初のノードを双方向連結リストから削除する。
# deleteFirst : 双方向連結リストの先頭のノードを削除する。
# deleteLast : 双方向連結リストの末尾のノードを削除する。
# それでは、各クラス・メソッド・変数の詳細を解説していきます。

# Node クラス
# Node クラスは、双方向連結リストのノードを表すクラスです。インスタンス変数として、key（ノードのキー）、next（次のノードを表す Node オブジェクト）、prev（前のノードを表す Node オブジェクト）を持ちます。

# DoublyLinkedList クラス
# DoublyLinkedList クラスは、双方向連結リストを表すクラスです。インスタンス変数として、sentinel（リストの先頭と末尾を示すダミーノードを表す Node オブジェクト）を持ちます。また、以下のメソッドを実装しています。

# __init__(self): sentinel を初期化する。
# insert(self, key): キーが key であるノードをリストの先頭に追加する。
# _deleteNode(self, node): ノード node をリストから削除する。内部的に使われるメソッドであり、delete()、deleteFirst()、deleteLast() の実装に使われる。
# delete(self, key): キーが key である最初のノードをリストから削除する。
# deleteFirst(self): リストの先頭のノードを削除する。
# deleteLast(self): リストの末尾のノードを削除する。
# print_key(self): リストの各ノードのキーを順に出力する。
# __init__ メソッド
# __init__ メソッドでは、sentinel という名前の Node オブジェクトを生成し、その next と prev をそれぞれ sentinel 自身に


# 福島悠介（Yusuke Fukushima）
# 続きをお願いします。
# このコードは、双方向連結リストを実装しています。具体的には、Nodeクラスが各ノードを表し、DoublyLinkedListクラスが双方向連結リスト全体を表しています。

# Nodeクラスでは、次のノードを指すnextと前のノードを指すprev、そしてそのノードの値を表すkeyを保持します。DoublyLinkedListクラスでは、双方向連結リストの全体を管理するためのメソッドを提供します。

# __init__メソッドでは、ダミーノードを作成して、そのノードのnextとprevをそれぞれ自身に設定しています。これにより、空の連結リストを作成します。

# insertメソッドでは、キー値keyを持つ新しいノードを作成し、双方向連結リストの先頭に追加します。具体的には、new_nodeに対して、self.sentinel.nextを次のノードとして、self.sentinelを前のノードとして設定し、self.sentinelとnew_nodeの間に新しいノードを追加します。

# deleteメソッドでは、指定されたキー値keyを持つ最初のノードを双方向連結リストから削除します。具体的には、指定されたキー値を持つノードを探し、そのノードを_deleteNodeメソッドに渡します。

# deleteFirstメソッドでは、双方向連結リストの先頭にあるノードを削除します。具体的には、ダミーノードのnextにあるノードを_deleteNodeメソッドに渡します。

# deleteLastメソッドでは、双方向連結リストの末尾にあるノードを削除します。具体的には、ダミーノードのprevにあるノードを_deleteNodeメソッドに渡します。

# print_keyメソッドでは、双方向連結リストのキーを出力します。具体的には、ダミーノードのnextから順番にノードのキーを出力し、最後のノードでは改行を出力します。

# 最後に、input関数を使って標準入力からデータを取得し、command_listに格納します。その後、command_listに従って、双方向連結リストの操作を実行します。最後に、双方向連結リストのキーを出力します。


# 福島悠介（Yusuke Fukushima）
# insert関数の下記部分をより詳細に教えてください。
# self.sentinel.next.prev = new_node
# self.sentinel.next = new_node
# insert関数のこの部分は、新しいノードをリストの先頭に挿入するために、次のような手順で実行されます。

# 新しいノードnew_nodeを作成します。
# new_nodeの次のノードを現在の先頭ノード(self.sentinel.next)に設定します。
# new_nodeの前のノードをリストの先頭にある特別なノードself.sentinelに設定します。この特別なノードは、リストの先頭(head)と末尾(tail)の両方を表すために使用されます。
# 現在の先頭ノード(self.sentinel.next)の前のノードを新しいノードnew_nodeに設定します。つまり、self.sentinel.nextの前のノードが新しいノードnew_nodeを指すようにします。
# self.sentinel.nextを新しいノードnew_nodeに設定します。つまり、特別なノードself.sentinelの次のノードが新しいノードnew_nodeを指すようにします。
# 上記の手順を組み合わせると、新しいノードをリストの先頭に追加することができます。self.sentinel.nextがNoneの場合、リストが空の場合には、特別なノードself.sentinelの前のノードも新しいノードnew_nodeに設定する必要があるため、self.sentinel.prevも新しいノードnew_nodeを指すようにします。


# 福島悠介（Yusuke Fukushima）
# こちらは、どのような仕組みで実装しているのでしょうか。
# self.sentinel.nextがNoneの場合、リストが空の場合には、特別なノードself.sentinelの前のノードも新しいノードnew_nodeに設定する必要があるため、self.sentinel.prevも新しいノードnew_nodeを指すようにします。
# 正確におっしゃる通りです。DoublyLinkedListのsentinel属性は、リストにおいて特別なノードを表しており、その前後に要素が追加されていきます。通常、双方向連結リストの先頭(head)や末尾(tail)は、単方向連結リストと同様に特別なノードで表現されますが、この実装ではsentinelが先頭と末尾を兼ねるようになっています。

# insertメソッドは、新しいノードを連結リストの先頭に挿入するためのものです。具体的には、新しいノードnew_nodeを作成し、self.sentinel.nextとself.sentinelの間に挿入します。そのために、new_nodeのprev属性にはself.sentinelを設定し、next属性にはself.sentinel.nextを設定します。そして、挿入前の先頭ノード(old_node)のprev属性にnew_nodeを、self.sentinelのnext属性にnew_nodeを設定することで、new_nodeを先頭ノードとして連結リストに挿入することができます。

# なお、もしリストが空の場合、つまりself.sentinel.nextがNoneの場合、新しいノードが先頭ノードかつ末尾ノードとなるため、self.sentinel.prevも新しいノードnew_nodeを指すようにする必要があります。したがって、先にself.sentinel.nextにnew_nodeを設定したあと、if文でself.sentinel.nextがNoneである場合には、self.sentinel.prevにもnew_nodeを設定しています。


# 福島悠介（Yusuke Fukushima）
# こちらの処理は、コード上ではどちらに該当しますでしょうか。
# if文でself.sentinel.nextがNoneである場合には、self.sentinel.prevにもnew_nodeを設定しています。
# この処理は、insert関数の中で行われています。具体的には、以下のようなコードブロックになります。

# lua
# Copy code
# # sentinel → old_node(旧self.sentinel.next) から
# # sentinel → new_node ⇔ old_node へ
# # self.sentinel.next = Noneの時のみ、self.sentinel.prevにもnew_nodeが入る。
# # self.sentinel.prevが常に末尾を指す
# self.sentinel.next.prev = new_node
# self.sentinel.next = new_node
# self.sentinelは、ダミーノードのインスタンスを保持しており、このダミーノードは、双方向の連結リストの先頭を表しています。この連結リストは、ノードが存在しない状態から始まる場合があります。この場合、リストの先頭に新しいノードを追加する必要がありますが、この際に、ダミーノードの前に新しいノードを追加する必要があることになります。

# このため、self.sentinel.nextがNoneの場合、リストが空の状態になるため、ダミーノードの前に新しいノードを追加する必要があるため、self.sentinel.prevにも新しいノードを設定しています。それ以外の場合には、単にself.sentinel.nextに新しいノードを追加するだけで十分です。


# 福島悠介（Yusuke Fukushima）
# ”self.sentinel.prevにも新しいノードを設定”の箇所が、コードでどのように実装されているかが分かりません。
# self.sentinel.prevに新しいノードを設定するのは、空の連結リストに新しいノードを追加する場合に必要です。この場合、現在のself.sentinel.next（つまり、None）に新しいノードを接続することになりますが、このときself.sentinel.prevは空リストの末尾を指す必要があります。そのため、self.sentinel.prevにも新しいノードを設定する必要があります。

# 具体的には、次のようになります。

# python
# Copy code
# # キーxのノードを生成
# # ノードを生成した時点でnode.nextに現HEAD, node.prevにNone(Node)を入れる)
# new_node = Node(key, self.sentinel.next, self.sentinel)

# if self.sentinel.next is None:  # リストが空の場合
#     self.sentinel.prev = new_node

# # sentinel → old_node(旧self.sentinel.next) から
# # sentinel → new_node ⇔ old_node へ
# # self.sentinel.prevが常に末尾を指す
# self.sentinel.next.prev = new_node
# self.sentinel.next = new_node
# このコードでは、self.sentinel.nextがNoneの場合（つまり、リストが空の場合）、新しいノードを生成してから、self.sentinel.prevに新しいノードを設定しています。その後、self.sentinel.nextとself.sentinel.prevのポインタを新しいノードに接続しています。
