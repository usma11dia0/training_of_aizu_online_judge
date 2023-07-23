# https://judge.u-aizu.ac.jp/onlinejudge/review.jsp?rid=7093165#1

# 2分探索木の特徴　参考：アルゴリズム図鑑(アプリ)
# 1. 全てのノードは、そのノードの左部分木に含まれるどの数よりも大きくなる
# 2. 全てのノードは、そのノードの右部分木に含まれるどの数よりも小さくなる

# 2分探索木にてノードを削除する場合
# 子ノードが一つもない場合：そのまま削除
# 子ノードが一つの場合：子ノードを削除ノードの場所へ移し替える
# 子ノードが二つの場合：削除ノードの左部分木から最大ノードを探索し、削除ノードの場所へ移し替える。
#                     ※削除ノードの右部分木から最小ノードを探索し、削除ノードの場所へ移し替えても可。

#二分探索木を実装
class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.right = None
        self.left = None

class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, key: int) -> None:
        if self.root is None:
            self.root = Node(key)
            return

        def _insert(node: Node, key: int) -> Node:
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            # 深さを戻す際は親ノードを返す
            return node
        
        _insert(self.root, key)
      
    def inorder(self) -> None:
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.key)
                _inorder(node.right)
        _inorder(self.root)

    
    def search(self, key: int) -> bool:
        def _search(node: Node, key: int) -> bool:
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            elif key > node.key:
                return _search(node.right, key)
        return _search(self.root, key)

    def min_key(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def remove(self, key: int) -> None:
        def _remove(node: Node, key: int) -> Node:
            if node is None:
                return node
            # 該当のkeyを持つノードを検索
            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            # 該当のkeyを持つノードが見つかった場合
            else:
                # 子ノードが一つもない場合、None
                # 子ノードが一つの場合、その子ノードを返す
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # 子ノードが二つの場合
                # 右部分木の最小値ノードを取得
                temp = self.min_key(node.right)
                # 削除するノードの値に最小値ノードの値をコピーして入れ替え
                node.key = temp.key
                # 右部分木から残った最小値ノードを削除
                node.right = _remove(node.right, temp.key)
            return node
        _remove(self.root, key)
         

if __name__ == '__main__':
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    binary_tree.inorder()
    print(binary_tree.search(7))
    binary_tree.remove(6)
    print('************ Remove')
    binary_tree.inorder()


    
        


