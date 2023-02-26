import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False

PRE_ORDER = 0
IN_ORDER = 1
POST_ORDER = 2

PRE = 3
IN = 4
POST = 5

node_list = []


def dfs(node_idx, order):
    c_n = node_list[node_idx]
    l_idx = c_n[1][0]
    r_idx = c_n[1][1]

    if order == PRE_ORDER:
        print(f" {node_idx}", end="")

    if l_idx < 0 and r_idx < 0:
        if order == IN_ORDER:
            print(f" {node_idx}", end="")
    else:
        if l_idx >= 0:
            dfs(l_idx, order)

        if order == IN_ORDER:
            print(f" {node_idx}", end="")

        if r_idx >= 0:
            dfs(r_idx, order)

    if order == POST_ORDER:
        print(f" {node_idx}", end="")

    return


def print_tree(root_idx, print_order):
    stack = [(root_idx, POST), (root_idx, PRE)]
    is_visited_idx_set = set()
    while stack:
        node_idx, order = stack.pop()
        cn = node_list[node_idx]
        l_idx = cn[1][0]
        r_idx = cn[1][1]

        if order == PRE:
            if print_order == PRE_ORDER:
                print(f" {node_idx}", end="")
            elif (
                print_order == IN_ORDER
                and l_idx < 0
                and node_idx not in is_visited_idx_set
            ):
                is_visited_idx_set.add(node_idx)
                print(f" {node_idx}", end="")

            if r_idx >= 0:
                stack.append((r_idx, POST))
                stack.append((node_idx, IN))
                stack.append((r_idx, PRE))
            if l_idx >= 0:
                stack.append((l_idx, POST))
                stack.append((node_idx, IN))
                stack.append((l_idx, PRE))
        elif (
            print_order == IN_ORDER
            and order == IN
            and node_idx not in is_visited_idx_set
        ):
            is_visited_idx_set.add(node_idx)
            print(f" {node_idx}", end="")
        elif print_order == POST_ORDER and order == POST:
            print(f" {node_idx}", end="")

    return


def main():
    if READ_FROM_FILE:
        f = open("test0.txt", "r")
    else:
        f = sys.stdin

    n = int(f.readline())
    global node_list
    node_list = [[-1, [-1, -1]] for _ in range(n)]
    for _ in range(n):
        i_list = list(map(int, f.readline().split()))
        p = i_list[0]
        l_idx = i_list[1]
        r_idx = i_list[2]
        node_list[p][1] = [l_idx, r_idx]
        if l_idx >= 0:
            node_list[l_idx][0] = p
        if r_idx >= 0:
            node_list[r_idx][0] = p

    root = -1
    for i in range(n):
        if node_list[i][0] == -1:
            root = i
            break

    print("Preorder")
    # dfs(root, PRE_ORDER)
    print_tree(root, PRE_ORDER)
    print()
    print("Inorder")
    # dfs(root, IN_ORDER)
    print_tree(root, IN_ORDER)
    print()
    print("Postorder")
    # dfs(root, POST_ORDER)
    print_tree(root, POST_ORDER)
    print()

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == "__main__":
    main()
