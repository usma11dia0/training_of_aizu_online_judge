# https://blog.ikappio.com/solve-minimum-cost-sort-using-cpp/#:~:text=%E7%B5%90%E6%A7%8B%E3%82%80%E3%81%9A%E3%81%8B%E3%81%97%E3%82%81%E3%80%82-,ALDS1_6_D%3A%20Minimum%20Cost%20Sort%3A%20%E6%9C%80%E5%B0%8F%E3%82%B3%E3%82%B9%E3%83%88%E3%82%BD%E3%83%BC%E3%83%88,%E3%81%8C%E3%81%8B%E3%81%8B%E3%82%8B%E3%80%81%E3%81%A8%E3%81%84%E3%81%86%E6%83%B3%E5%AE%9A%E3%81%A7%E3%81%99%E3%80%82


def min_cost_sort(w_list: list, sort_list: list) -> int:
    ans = 0
    min_num = sort_list[0]
    for i in range(len(w_list)):
        # x:  w_list[i]のソート後のindex
        x = sort_list.index(w_list[i])
        if x == i:
            continue
        sum_cost = 0
        min_gnum = 10**4 + 1
        # j: whileループ内のiterator
        j = i
        loop_count = 0
        while True:
            # 方法1 : 未ソート要素の連鎖によりグループ分けし、グループの最小値を常に用いて入れ替えを行う
            # 例：[6,3,4,2,1,5] → [6, 5, 1], [3, 4, 2]とグループ分けを行い、左グループは1/右グループは2を常に用いて入れ替えを行う。
            loop_count += 1
            # 最小値 ⇔ w_list[j]の入れ替えの際に発生するw_list[j]側のコストを加算
            sum_cost += w_list[j]
            min_gnum = min(min_gnum, w_list[j])
            if x == i:
                break
            w_list[x], w_list[j] = w_list[j], w_list[x]
            x = sort_list.index(w_list[j])

        # 1 or 2 のうち小さいほうをansへ加算
        # 方法1の入れ替えコスト = min_gnum以外の総和  + (入れ替え回数 - 1) * min_gnum
        # (入れ替え回数 - 1) : 最後の1→6のループは入れ替え回数に含めないため-1にする。
        cost_1 = (sum_cost - min_gnum) + (loop_count - 1) * min_gnum

        # 方法2 : グループ内へリストの最小値を加え、リストの最小値を常に用いて入れ替えを行う
        # 例：[6,3,4,2,1,5] → [6, 5, 1, 1], [3, 4, 2, 1]とグループ分けを行い、それぞれ1を常に用いて入れ替えを行う。
        # 方法2の入れ替えコスト = min_gnum以外の総和  + (入れ替え回数 - 1) * min_num + (min_gnumとmin_numの入れ替えコスト) * 2
        # (min_gnumとmin_numの入れ替えコスト) * 2: リストの最小値をグループへ加える/除くための入れ替え
        cost_2 = (
            (sum_cost - min_gnum)
            + (loop_count - 1) * min_num
            + (min_gnum + min_num) * 2
        )
        ans += min(cost_1, cost_2)
    return ans


n = int(input())
w_list = list(map(int, input().split()))
sort_list = sorted(w_list)

print(min_cost_sort(w_list, sort_list))
