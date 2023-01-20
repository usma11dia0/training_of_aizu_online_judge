# 入力データの取得
n = int(input())
have_cards = [list(map(str, input().split())) for _ in range(0, n)]

# 辞書の生成
card_dict = {"S": set(), "H": set(), "C": set(), "D": set()}
no_card_dict = {"S": set(), "H": set(), "C": set(), "D": set()}
card_marks = {"S", "H", "C", "D"}

# 持っているカードをcard_dictへ追加
for mark, num in have_cards:
    card_dict[mark].add(num)

# 持っていないカードをリスト内包表記で出力
for mark in card_marks:
    for num in range(1, 14):
        if str(num) not in card_dict[mark]:
            no_card_dict[mark].add(num)

print(*no_card_dict)

# no_card_dict = [
#     no_card_dict[mark].add(num)
#     for num in range(1, 14)
#     for mark in card_marks
#     if str(num) not in card_dict[mark]
# ]


# no_card_list = [         for mark in card_marks]
