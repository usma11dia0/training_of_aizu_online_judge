# https://aotamasaki.hatenablog.com/entry/2019/11/03/%E8%9E%BA%E6%97%8B%E6%9C%AC%E3%82%92Python%E3%81%A7%E8%A7%A3%E3%81%8F_Part2


class Node:
    def __init__(self, parent: int, children: list, depth: int, type: str):
        self.parent = parent
        self.children = children
        self.depth = depth
        self.type = type


def print_result(T: dict) -> None:
    for i in range(len(T)):
        output = f"node {i}: "
        output += f"parent = {T[i].parent}, "
        output += f"depth = {T[i].depth}, "
        output += f"{T[i].type}, "
        output += f"{T[i].children}"
        print(output)


n = int(input())

# キーを節点番号, 値をNodeとした辞書を生成
T = {i: Node(-1, [], -1, "") for i in range(0, n)}

# T内のNodeへ入力データから得られる情報を追記
for _ in range(0, n):
    node_info = list(map(int, input().split()))

    # 子ノードの有無で場合分け
    if node_info[1] != 0:
        # ノード_info[0]に対する処理
        T[node_info[0]].type = "internal node"
        T[node_info[0]].children = node_info[2:]
        # ノード_info[0]の子ノードに対する処理
        for child in T[node_info[0]].children:
            # 節点番号のノードを親ノードとして追記
            T[child].parent = node_info[0]
    else:
        T[node_info[0]].type = "leaf"

# 深さを導出
for i in range(0, n):
    depth = 0
    node_id = i
    # 初期値の-1が更新されていなければroot
    if T[node_id].parent == -1:
        T[i].depth = 0
        T[i].type = "root"
    else:
        # rootに辿り着くまで子→親へ遡る
        while T[node_id].parent != -1:
            node_id = T[node_id].parent
            depth += 1
        T[i].depth = depth


print_result(T)
