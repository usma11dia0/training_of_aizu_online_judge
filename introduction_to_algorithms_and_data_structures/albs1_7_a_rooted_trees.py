# https://aotamasaki.hatenablog.com/entry/2019/11/03/%E8%9E%BA%E6%97%8B%E6%9C%AC%E3%82%92Python%E3%81%A7%E8%A7%A3%E3%81%8F_Part2

import sys

sys.setrecursionlimit(2**20)  # 再帰回数上限の向上 かなり多くしないとREになる


class Node:
    def __init__(self, parent: int, children: list, depth: int, type: str):
        self.parent = parent
        self.children = children
        self.depth = depth
        self.type = type


# 深さ優先探索
def _dfs(pos, T, visited):
    visited[pos] = True
    for i in T[pos]:
        if visited[i] == False:
            cnt += _dfs(1, T, visited)
    return 1


def get_depth(node_index: int, T: dict) -> int:
    visited = [False] * (len(T) + 1)
    depth = _dfs(0, T, visited)
    return depth


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

    # 子のノードを持たない場合は次へ
    if node_info[1] == 0:
        T[node_info[0]].type = "leaf"
        continue

    # 節点番号が0であれば親ノード
    if node_info[0] == 0:
        T[node_info[0]].parent = -1
        T[node_info[0]].depth = 0
        T[node_info[0]].type = "root"
        continue

    # 節点番号のノードの子ノードを追記
    T[node_info[0]].children = node_info[2:]

    # 節点番号のノードを親ノードとして追記
    for child in T[node_info[0]].children:
        T[child].parent = node_info[0]

    T[node_info[0]].type = "internal node"

print_result(T)
