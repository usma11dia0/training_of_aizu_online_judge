# 二分木と二分探索木は違う(二分木には子ノードの配置や順序に制約なし)

class Node:
    def __init__(self, key: int) -> None:
        self.key = key
        self.left = None
        self.right = None

def build_tree(preorder:list, inorder:list) -> Node:
    if inorder:
        # ルートはpreorderの最初の要素
        root = Node(preorder[0])
        # ルートの位置をinorder内で見つける
        index = inorder.index(root.key)
        # 左部分木と右部分木を再帰的に構築
        root.left = build_tree(preorder[1:index + 1], inorder[:index])
        root.right = build_tree(preorder[index + 1:], inorder[index + 1:])
        return root
    return None

def postorder(node: Node) -> None:
    def _postorder(node: Node) -> None:
        if node is not None:
            _postorder(node.left)
            _postorder(node.right)
            output.append(str(node.key))
    output = []
    _postorder(node)
    print(' '.join(output))


m = int(input())
preorder_list = list(map(int, input().split()))
inorder_list = list(map(int, input().split()))

root = build_tree(preorder_list, inorder_list)
postorder(root)



        
# if __name__ == '__main__':
#     preorder = [1, 2, 3, 4, 5]
#     inorder = [3, 2, 4, 1, 5]
#     root = build_tree(preorder, inorder)
#     print(root.left.left.key)
#     postorder(root)


# 例えば、次のような preorder と inorder のシーケンスが与えられたとします：

# preorder: 1 2 4 7 3 5 8 6
# inorder: 7 4 2 1 5 3 8 6

# preorderを見て、rootは1。

# inorderとrootが1であることから、rootの左部分木は、742の列になり、右部分木は、5386の列になる。

# ここで、rootの左部分木と右部分木の範囲が確定しますが、まだ詳細な構造はわかりません。

# preorderで742が出てくる部分は2番目から4番目なので、preorderの列は、247となる。

# preorder=247、inorder=742として1に戻る。

# preorderより、部分木の根root_partは2。

# inorderとroot_partが2であることから、root_partの左部分木は、74となり、右部分木は空となる。

# preorderで74が出てくる部分は3番目から4番目なので、preorderの列は、47となる。

# preorder=47、inorder=74として1に戻る。

# preorderより、部分木の根root_partは4。

# inorderとroot_partが4であることから、root_partの左部分木は、7となり、右部分木は空となる。

# ここで、root_partの左部分木が確定します。左の子が7。右の子は存在しません。

# この結果、元のrootの左部分木ができました。

# 同様の手順を元のrootの右部分木に対して実行します：

# preorderで5386が出てくる部分は5番目から8番目なので、preorderの列は、3586となる。

# preorder=3586、inorder=5386として、元の手順1から再度開始します。

# 最終的なバイナリツリーの構造は次のようになります：

# markdown
# Copy code
#         1
#        / \
#       2   3
#      /   / \
#     4   5   6
#    /       /
#   7       8 

# ① 上記の例にて、7のノードまで再帰が進んだ場合、
#   root.left と root.rightが共にNone
# ➁ 最後はrootをリターンして深さを戻す
# ④ 深さを戻した際、root(4).leftに7(root)が入る


# inorderのインデックス番号で、preorderの分割ができる理由
# inorderのインデックス番号 = 左部分木のノードの数
# preorderからrootの1を除いた1:index+1までの範囲が左部分木であることがわかる。