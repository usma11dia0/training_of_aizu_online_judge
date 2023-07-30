def print_complete_binary_tree(h: int, a: list) -> None:
    for i in range(0, h):
        key = a[i]
        parent_key = a[(i - 1)//2]
        left_key = a[2 * (i - 1)]
        right_key = a[2 * i]
        if i == 0:
            print(f'node {i}: key = {key}, left key = {left_key}, right key = {right_key}')
        elif left_key is None and right_key is None:
            print(f'node {i}: key = {key}, parent key = {parent_key}')
        elif left_key is None:
            print(f'node {i}: key = {key}, parent key = {parent_key}, right key = {right_key}')
        elif right_key is None:
            print(f'node {i}: key = {key}, parent key = {parent_key}, left key = {left_key}')
        else:        
            print(f'node {i}: key = {key}, parent key = {parent_key}, left key = {left_key}, right key = {right_key}')

if __name__ == "__main__":
    h = int(input())
    a = list(map(int, input().split()))
    print(h, a)
    print_complete_binary_tree(h, a)