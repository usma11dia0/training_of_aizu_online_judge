# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_C&lang=ja

# 入力データの取得
n = int(input())
taro_cards = [None] * n
hanako_cards = [None] * n
for i in range(0, n):
    taro_cards[i], hanako_cards[i] = input().split()

# 各カードを比較して両者の得点を算出
taro_score = 0
hanako_score = 0
for taro_card, hanako_card in zip(taro_cards, hanako_cards):
    is_calculated = False
    for i in range(min(len(taro_card), len(hanako_card))):
        # 先頭の文字列からASCIIコードの大小を比較。大小が確定したらその時点で処理を終了する。
        if ord(taro_card[i]) < ord(hanako_card[i]):
            hanako_score += 3
            is_calculated = True
            break
        elif ord(hanako_card[i]) < ord(taro_card[i]):
            taro_score += 3
            is_calculated = True
            break

    # 最後まで比較が続いた時は、文字列の長さで得点を判定する。
    if is_calculated == False:
        if len(taro_card) == len(hanako_card):
            hanako_score += 1
            taro_score += 1
        elif len(taro_card) < len(hanako_card):
            hanako_score += 3
        elif len(hanako_card) < len(taro_card):
            taro_score += 3

# 結果を出力
print(taro_score, hanako_score)
