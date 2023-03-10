# https://qiita.com/nyankiti/items/f593765cf4aca9cc2db2
# https://blog.ikappio.com/data-structure-tree-reconstruction-of-a-tree/


class Node:
    def __init__(
        self,
        id: int,
        parent: int,
        left: int,
        right: int,
    ):
        self.id = id
        self.parent = parent
        self.left = left
        self.right = right


# 深さ優先探索(後行順巡回)
def postorder(T: dict, u: int, l: list = []) -> list:
    if T[u].left != -1:
        postorder(T, T[u].left)
    if T[u].right != -1:
        postorder(T, T[u].right)
    l.append(T[u].id)
    # print(f"{T[u].id}", end=" ")
    return l


def reconstruction(preorder: list, inorder: list, parent: int) -> int:

    # 末尾再帰
    if len(preorder) == 0:
        return -1

    # rootの導出
    # preorderの0番目は必ず部分木の節点
    root = preorder[0]
    T[root].id = root
    T[root].parent = parent

    # 末尾再帰
    if len(preorder) == 1:
        return root

    # inorder内におけるrootのインデックスより左分木と右分木に分割
    sep = inorder.index(root)
    left_inorder = inorder[:sep]
    right_inorder = inorder[sep + 1 :]

    # 上記の左分木と右分木のそれぞれに対応するpreorderの列を生成
    left_preorder = [i for i in preorder if i in left_inorder]
    right_preorder = [i for i in preorder if i in right_inorder]

    # 左分木と右分木のそれぞれに対して再帰で繰り返す。
    T[root].left = reconstruction(left_preorder, left_inorder, parent)
    T[root].right = reconstruction(right_preorder, right_inorder, parent)

    return root


n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))

# キーを節点番号, 値をNodeとした辞書を生成 ※1-indexed
T = {i: Node(-1, -1, -1, -1) for i in range(1, n + 1)}

reconstruction(preorder, inorder, -1)

# 結果の出力
print(*postorder(T, preorder[0]))
