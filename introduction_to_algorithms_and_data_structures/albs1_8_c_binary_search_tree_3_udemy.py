import sys

class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
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
    
    def find(self, key) -> bool:
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

    def min_key(self, node) -> Node:
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete(self, key) -> None:
        def _delete(node: Node, key: int) -> Node:
            if node is None:
                return node
            # keyの値を持つノードを探索
            if key < node.key:
                node.left = _delete(node.left, key)
            elif key > node.key:
                node.right = _delete(node.right, key)
            # keyの値を持つノードが見つかった場合
            else:
                # 子ノードが一つもない場合：None
                # 子ノードが一つの場合：子ノード
                # を代入
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                # 子ノードが二つの場合
                # 右部分木の最小値ノードを取得
                tmp = self.min_key(node.right)
                # 削除するノードの値へ最小値ノードの値をコピー
                node.key = tmp.key
                # 右部分木内に残った最小値ノードを削除
                node.right = _delete(node.right, tmp.key)
            return node
        _delete(self.root, key)

    def print(self) -> str:
        #中間順巡回(inorder)を出力
        def inorder(node: Node) -> None:
            if node is not None:
                inorder(node.left)
                output.append(str(node.key))
                inorder(node.right) 
        #先行順巡回(preorder)を出力
        def preorder(node: Node) -> None:
            if node is not None:
                output.append(str(node.key))
                preorder(node.left)
                preorder(node.right)
        
        output = []
        inorder(self.root)
        inorder_output = " ".join(output)
        output = []
        preorder(self.root)
        preorder_output = " ".join(output)

        return " " + inorder_output + "\n" + " " + preorder_output


m = int(input())
T = BinarySearchTree()
output = []

for _ in range(0, m):
    command = sys.stdin.readline().split()
    if command[0] == "insert":
        T.insert(int(command[1]))
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


# for command in command_list:
#     if command[0] == "insert":
#         T.insert(int(command[1]))
#     elif command[0] == "find":
#         if T.find(int(command[1])) == True:
#             print("yes")
#         else:
#             print("no")
#     elif command[0] == "delete":
#         T.delete(int(command[1]))
#     elif command[0] == "print":
#         T.print()


# if __name__ == "__main__":
#     binary_tree = BinarySearchTree()
#     binary_tree.insert(8)
#     binary_tree.insert(2)
#     binary_tree.insert(3)
#     binary_tree.insert(7)
#     binary_tree.insert(22)
#     binary_tree.insert(1)
#     print(binary_tree.find(1))
#     print(binary_tree.find(2))
#     binary_tree.print()
#     binary_tree.delete(3)
#     binary_tree.delete(7)
#     binary_tree.print()

