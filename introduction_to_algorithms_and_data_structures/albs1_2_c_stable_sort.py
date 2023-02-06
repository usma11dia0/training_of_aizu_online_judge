# 関数定義
def bubbleSort(card_list: list) -> list:
    sorted_card_list = list(card_list)
    # card_listを昇順にソート
    for i in range(len(sorted_card_list) - 1, -1, -1):
        for j in range(0, i):
            if sorted_card_list[j][1] > sorted_card_list[j + 1][1]:
                sorted_card_list[j], sorted_card_list[j + 1] = (
                    sorted_card_list[j + 1],
                    sorted_card_list[j],
                )
    return sorted_card_list


def selectionSort(card_list: list) -> list:
    sorted_card_list = list(card_list)
    for i in range(0, len(sorted_card_list)):
        min_index = i
        for j in range(i, len(sorted_card_list)):
            if sorted_card_list[j][1] < sorted_card_list[min_index][1]:
                min_index = j
        sorted_card_list[i], sorted_card_list[min_index] = (
            sorted_card_list[min_index],
            sorted_card_list[i],
        )
    return sorted_card_list


def is_stable(card_list: list, sorted_card_list: list) -> bool:
    # それぞれのリストから数字が同じカードを抽出
    # 同じ数字のカードを格納する配列。要素番号がカードの数字に対応。
    same_number_cards = [[None] for _ in range(0, len(card_list))]
    sorted_same_number_cards = [[None] for _ in range(0, len(sorted_card_list))]

    for i in range(0, len(card_list)):
        for j in range(i + 1, len(card_list)):
            if card_list[i][1] == card_list[j][1]:
                # すでにリストに追加されている要素についてはスキップ
                if card_list[i] not in same_number_cards[int(card_list[i][1])]:
                    same_number_cards[int(card_list[i][1])].append(card_list[i])
                if card_list[j] not in same_number_cards[int(card_list[i][1])]:
                    same_number_cards[int(card_list[i][1])].append(card_list[j])

    for i in range(0, len(sorted_card_list)):
        for j in range(i + 1, len(sorted_card_list)):
            if sorted_card_list[i][1] == sorted_card_list[j][1]:
                if (
                    sorted_card_list[i]
                    not in sorted_same_number_cards[int(sorted_card_list[i][1])]
                ):
                    sorted_same_number_cards[int(sorted_card_list[i][1])].append(
                        sorted_card_list[i]
                    )
                if (
                    sorted_card_list[j]
                    not in sorted_same_number_cards[int(sorted_card_list[i][1])]
                ):
                    sorted_same_number_cards[int(sorted_card_list[i][1])].append(
                        sorted_card_list[j]
                    )

    # 抽出したリストの要素をそれぞれ比較
    for same_card, sorted_same_card in zip(same_number_cards, sorted_same_number_cards):
        if (
            len(same_card) > 1 and len(sorted_same_card) > 1
        ):  # 同じカードが格納されている場合、lenは1より大きい
            for i in range(1, len(same_card)):
                if same_card[i] != sorted_same_card[i]:
                    return False
    return True


# 入力データの取得
N = int(input())
card_list = list(input().split())

sorted_card_list = bubbleSort(card_list)
sorted_card_list_2 = selectionSort(card_list)

print(*sorted_card_list)
if is_stable(card_list, sorted_card_list):
    print("Stable")
else:
    print("Not stable")
print(*sorted_card_list_2)
if is_stable(card_list, sorted_card_list_2):
    print("Stable")
else:
    print("Not stable")
