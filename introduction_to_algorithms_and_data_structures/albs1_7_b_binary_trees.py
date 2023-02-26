# https://aotamasaki.hatenablog.com/entry/2019/11/03/%E8%9E%BA%E6%97%8B%E6%9C%AC%E3%82%92Python%E3%81%A7%E8%A7%A3%E3%81%8F_Part2

# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_preorder/print.html
# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_inorder/print.html
# https://yutaka-watanobe.github.io/star-aida/1.0/algorithms/btree_postorder/print.html


class Node:
    def __init__(
        self,
        parent: int,
        sibling: int,
        degree: int,
        depth: int,
        height: int,
        type: str,
        left: int,
        right: int,
    ):
        self.parent = parent
        self.sibling = sibling
        self.degree = degree
        self.depth = depth
        self.height = height
        self.type = type
        self.left = left
        self.right = right


def print_result(T: dict) -> None:
    for i in range(len(T)):
        output = f"node {i}: "
        output += f"parent = {T[i].parent}, "
        output += f"sibling = {T[i].sibling}, "
        output += f"degree = {T[i].degree}, "
        output += f"depth = {T[i].depth}, "
        output += f"height = {T[i].height}, "
        output += f"{T[i].type}"
        print(output)


# 入力データの取得
n = int(input())

# キーを節点番号, 値をNodeとした辞書を生成
T = {i: Node(-1, -1, 0, 0, 0, -1, -1, "") for i in range(0, n)}

# T内のNodeへ入力データから得られる情報を追記
for _ in range(0, n):
    node_info = list(map(int, input().split()))


# 結果の出力
print_result(T)
