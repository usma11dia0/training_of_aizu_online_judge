# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_C&lang=ja

# for i in range(97, 123):
#     print(chr(i))

# 数値 → 文字変換

# 文字 → 数値変換
# ord()

# 入力データの取得
target_str = ""
try:
    while True:
        t = str(input())  # 一文字ずつ取得
        if t == "":  # 最後は改行ではなく空白になる
            break
        target_str += t
except EOFError:  # 改行は無視する
    pass

# 入力データを小文字に統一
target_str_lower = target_str.lower()

# 配列の生成
alphabet_list = [chr(i) for i in range(97, 123)]
count_list = [0] * 26  # 要素0 → a, 要素25 → zにそれぞれ対応

# count_listへtarget_strの文字数を入れる
for s in target_str_lower:
    # sが[a-z]以外であれば無視
    if 97 <= ord(s) < 123:
        count_list[ord(s) - 97] += 1

for i in range(len(alphabet_list)):
    print(f"{alphabet_list[i]} : {count_list[i]}")
