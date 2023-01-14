# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_9_B&lang=ja

# 関数定義
def shuffle(card: str, ord_num: int) -> str:
    target = card[:ord_num]
    shuffled = card[ord_num:]
    shuffled += target
    return shuffled


# 入力データの取得
target_card = ""
result = []
while True:
    target_card = str(input())
    if target_card == "-":
        break
    m = int(input())
    for i in range(0, m):
        h = int(input())
        target_card = shuffle(target_card, h)
    result.append(target_card)

# 結果の出力
for r in result:
    print(r)
