# 最大積載量(load_cap)のトラックを何台用いれば運搬可能かを導出(cnt_track)し、
# 与えらえた条件のトラック数(k)と比較。
def is_carry(mid: int, w_list: list, k: int) -> bool:
    load_cap = mid
    sum_w = 0
    cnt_track = 1
    for w in w_list:
        # 荷物一つの重量が最大積載量を超える時、運搬不可
        if w > load_cap:
            return False
        sum_w += w
        # 荷物の総重量が最大積載量を超えた時、新たなトラックに荷物を積む
        while sum_w > load_cap:
            cnt_track += 1
            sum_w = w
    if cnt_track <= k:
        return True
    else:
        return False


# 入力データの取得
n, k = map(int, input().split())
w_list = [int(input()) for _ in range(0, n)]

ng = 0
ok = 10**9 + 1

# 二分探索の実施
while ok - ng > 1:
    mid = (ok + ng) // 2
    if is_carry(mid, w_list, k):
        ok = mid
    else:
        ng = mid

print(ok)
