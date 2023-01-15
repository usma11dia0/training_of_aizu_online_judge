# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_A

# さいころの各変数の意味
# top：上の面
# front：手前の面
# right: 右の面
# left: 左の面
# back：奥の面
# bottom：下の面

# classの定義
class Dice:
    face_val = ["top", "front", "right", "left", "back", "bottom"]

    def __init__(self, face_list: list, face_val: list = face_val) -> None:
        self.face_dict = dict(zip(face_val, face_list))

    def roll(self, orders: str) -> dict:
        for order in orders:
            # 値渡しで辞書型をコピーする
            current_face_dict = self.face_dict.copy()
            # 縦回転(上方向) ※rightとleftは変化なし
            if order == "N":
                self.face_dict["top"] = current_face_dict["front"]
                self.face_dict["front"] = current_face_dict["bottom"]
                self.face_dict["back"] = current_face_dict["top"]
                self.face_dict["bottom"] = current_face_dict["back"]
            # 縦回転(下方向) ※上方向と対
            elif order == "S":
                self.face_dict["top"] = current_face_dict["back"]
                self.face_dict["front"] = current_face_dict["top"]
                self.face_dict["back"] = current_face_dict["bottom"]
                self.face_dict["bottom"] = current_face_dict["front"]
            # 横回転(右方向) ※frontとbackは変化なし
            elif order == "E":
                self.face_dict["top"] = current_face_dict["left"]
                self.face_dict["right"] = current_face_dict["top"]
                self.face_dict["left"] = current_face_dict["bottom"]
                self.face_dict["bottom"] = current_face_dict["right"]
            # 横回転(左方向) ※右方向と対
            elif order == "W":
                self.face_dict["top"] = current_face_dict["right"]
                self.face_dict["right"] = current_face_dict["bottom"]
                self.face_dict["left"] = current_face_dict["top"]
                self.face_dict["bottom"] = current_face_dict["left"]
        return self.face_dict

    def top_face(self):
        return self.face_dict["top"]


# 入力データの取得
face_list = list(map(int, input().split()))
orders = str(input())

dice = Dice(face_list)
dice.roll(orders)
print(dice.top_face())
