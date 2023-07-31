def print_complete_binary_tree(h: int, a: list) -> None:
    for i in range(0, h):
        key = a[i]
        parent_key = a[(i + 1) // 2 - 1]
        left_key = a[2 * i + 1] if 2 * i + 1 < h else None
        right_key = a[2 * i + 2] if 2 * i + 2 < h else None
        if i == 0:
            print(f'node {i + 1}: key = {key}, left key = {left_key}, right key = {right_key}, ')
        elif left_key is None and right_key is None:
            print(f'node {i + 1}: key = {key}, parent key = {parent_key}, ')
        elif left_key is None:
            print(f'node {i + 1}: key = {key}, parent key = {parent_key}, right key = {right_key}, ')
        elif right_key is None:
            print(f'node {i + 1}: key = {key}, parent key = {parent_key}, left key = {left_key}, ')
        else:        
            print(f'node {i + 1}: key = {key}, parent key = {parent_key}, left key = {left_key}, right key = {right_key}, ')

h = int(input())
a = list(map(int, input().split()))
print_complete_binary_tree(h, a)