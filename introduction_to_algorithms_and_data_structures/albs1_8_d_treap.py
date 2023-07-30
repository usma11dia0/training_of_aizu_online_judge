import sys

class Node:
    def __init__(self, key: int, priority: int) -> None:
        self.key = key
        self.priority = priority
        self.right = None
        self.left = None

class Treap:
    def __init__(self) -> None:
        self.root = None
    
    def _right_rotate(self, old_root: Node) -> Node:
        # 対象部分木のrootを入れ替え
        new_root = old_root.left
        # old_rootの左子ノードにnew_rootの右子ノードを挿入
        # ※二分探索木の条件を満たすため
        old_root.left = new_root.right
        # new_rootの右子ノードにold_rootを挿入
        new_root.right = old_root
        return new_root
    
    def _left_rotate(self, old_root: Node) -> Node:
        new_root = old_root.right
        old_root.right = new_root.left
        new_root.left = old_root
        return new_root

    def insert(self, key: int, priority: int) -> None:
        if self.root is None:
            self.root = Node(key, priority)
            return
        def _insert(node: Node, key:int, priority: int) -> None:
            # 再帰終了条件
            # 子ノードがない時に挿入位置確定
            if node is None:
                return Node(key, priority)
            if key < node.key:
                node.left = _insert(node.left, key, priority)
                # 左の子の方が優先度が高い場合、右回転
                if node.priority < node.left.priority:
                    node = self._right_rotate(node)
            else:
                node.right = _insert(node.right, key, priority)
                # 右の子の方が優先度が高い場合、左回転
                if node.priority < node.right.priority:
                    node = self._left_rotate(node)

            # 深さを戻す際に親ノードを返す
            return node
    
        self.root = _insert(self.root, key, priority)
    
    def find(self, key: int) -> bool:
        def _find(node: Node, key: int) -> bool:
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _find(node.left, key)
            else:
                return _find(node.right, key)
        
        return _find(self.root, key)

    def delete(self, key:int) -> None:
        def _delete(node: Node, key: int) -> Node:
            if node is None:
                return None
            # keyの値を持つノードを探索
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            # keyの値を持つノードが見つかった時
            else:
                # 葉の場合
                if node.left is None and node.right is None:
                  return None
                # 右の子のみを持つ場合左回転
                elif node.left is None:
                    node = self._left_rotate(node)
                # 左の子のみを持つ場合右回転
                elif node.right is None:
                    node = self._right_rotate(node)
                # 両方の子を持つ場合
                else:
                    # 優先度の高い方を持ち上げる
                    if node.left.priority > node.right.priority:
                        node = self._right_rotate(node)
                    else:
                        node = self._left_rotate(node)
                return _delete(node, key)
            return node
        
        self.root = _delete(self.root, key)
    
    def print(self) -> str:
        # 中間順巡回(inorder)を出力
        def _inorder(node: Node) -> None:
            if node is not None:
                _inorder(node.left)
                output.append(str(node.key))
                _inorder(node.right)
        # 先行順巡回(preorder)を出力
        def _preorder(node: Node) -> None:
            if node is not None:
                output.append(str(node.key))
                _preorder(node.left)
                _preorder(node.right)
        
        output=[]
        _inorder(self.root)
        inorder_output = " ".join(output)
        output=[]
        _preorder(self.root)
        preorder_output = " ".join(output)

        return " " + inorder_output + "\n" + " " + preorder_output
    

m = int(input())
T = Treap()
output = []

for _ in range(0, m):
    command = sys.stdin.readline().split()
    if command[0] == "insert":
        T.insert(int(command[1]), int(command[2]))
    elif command[0] == "find":
        if T.find(int(command[1])):
            output.append("yes")
        else:
            output.append("no")
    elif command[0] == "delete":
        T.delete(int(command[1]))
    elif command[0] == "print":
        output.append(T.print())

print("\n".join(output))