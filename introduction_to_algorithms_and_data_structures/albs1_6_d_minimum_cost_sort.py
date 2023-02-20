def solve(w_list, sort_list):
    ans = 0
    min_num = sort_list[0]
    for i in range(len(w_list)):
        x = sort_list.index(w_list[i])  # w_list[i]がsort_listの何番目に格納されているかを返す。
        if x == i:  # w_listとsort_listの要素番号が同じ = swapの必要なし。
            continue
        sum_cost = 0
        min_loop_n = 10**4 + 1
        j = i  # whileループのiterator
        loop_count = 0  # ?
        while True:
            loop_count += 1
            sum_cost += w_list[j]
            min_loop_n = min(min_loop_n, w_list[j])
            if x == i:
                break
            w_list[x], w_list[j] = w_list[j], w_list[x]
            x = sort_list.index(w_list[j])
        ans += min(
            sum_cost + (loop_count - 2) * min_loop_n,
            sum_cost + min_loop_n + (loop_count + 1) * min_num,
        )
    return ans


n = int(input())
w_list = list(map(int, input().split()))
sort_list = sorted(w_list)
print(solve(w_list, sort_list))
