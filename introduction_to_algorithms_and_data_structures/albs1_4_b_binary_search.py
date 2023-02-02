def is_low(mid: int, S: list, target: int) -> int:
    if target < S[mid]:
        return 1
    elif target > S[mid]:
        return 0
    elif target == S[mid]:
        return -1


# 入力データの取得
n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


cnt = 0
for t in T:
    ng = -1
    ok = len(S)
    # 二分探索でtがSに含まれるかを判定
    while ok - ng > 1:
        mid = (ng + ok) // 2
        result = is_low(mid, S, t)
        if result == -1:
            cnt += 1
            break
        elif result == 1:
            ok = mid
        elif result == 0:
            ng = mid

print(cnt)
