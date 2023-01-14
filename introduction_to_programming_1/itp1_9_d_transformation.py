# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_D&lang=ja

# 関数定義
def order_print(s: str, a: int, b: int) -> None:
    print(s[a : b + 1])


def order_replace(s: str, a: int, b: int, rep: str) -> str:
    # 一度リストへ変換してから一文字ずつ入れ替える
    list_s = list(s)
    for i in range(a, b + 1):
        list_s[i] = rep[i - a]
    return "".join(list_s)


def order_reverse(s: str, a: int, b: int) -> str:
    # a～b文字目を抜き出し逆順にする
    slice_s = s[a : b + 1]
    reverse_s = ""
    for i in range(len(slice_s) - 1, -1, -1):
        reverse_s += slice_s[i]
    # a～bをreverse_sに入れ替える
    return order_replace(s, a, b, reverse_s)


# 入力データの取得
string = str(input())
q = int(input())
order_list = [list(input().split()) for _ in range(0, q)]

for order in order_list:
    a = int(order[1])
    b = int(order[2])
    if order[0] == "print":
        order_print(string, a, b)
    elif order[0] == "reverse":
        string = order_reverse(string, a, b)
    elif order[0] == "replace":
        rep_str = order[3]
        string = order_replace(string, a, b, rep_str)
