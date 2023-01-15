# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_11_B&lang=ja

# さいころの各変数の意味
# top：上の面
# front：手前の面
# right: 右の面
# left: 左の面
# back：奥の面
# bottom：下の面

# classの定義
class Dice:
    # クラス変数
    face_val = ["top", "front", "right", "left", "back", "bottom"]

    def __init__(self, face_list: list, face_val: list = face_val) -> None:
        self.face_dict = dict(zip(face_val, face_list))
        self.face_top_list = []
        self.face_all_list = []

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

    # 全探索
    def all_face(self):
        ## 1. topがそれぞれ1～6の組み合わせを導出
        # 初期状態を保持
        init_face_dict = self.face_dict.copy()
        self.face_top_list.append(init_face_dict)
        # NSWE方向にそれぞれ一回ずつrollする
        for s in "NSWE":
            self.face_top_list.append(self.roll(s))
            # rollによるface_dictの変更取り消し
            self.face_dict = init_face_dict.copy()
        # Topが元々bottomだった場合のみ別途導出 ※同一方向に2回rollする。
        self.face_top_list.append(self.roll("NN"))
        # rollによるface_dictの変更取り消し
        self.face_dict = init_face_dict.copy()

        ## 2. topを固定して側面の組み合わせ(4通り)をそれぞれ導出
        for face_top in self.face_top_list:
            self.face_dict = face_top.copy()
            for s in "NNNN":
                dict_tmp = self.roll(s).copy()
                self.face_all_list.append(dict_tmp)
                self.face_dict = dict_tmp.copy()
        # rollによるface_dictの変更取り消し
        self.face_dict = init_face_dict.copy()

        return self.face_all_list

    def top_face(self) -> int:
        return self.face_dict["top"]

    def right_face(self, top: int, front: int) -> int:
        for face_list in self.face_all_list:
            if (face_list["top"] == top) and (face_list["front"] == front):
                return face_list["right"]


# 入力データの取得
face_list = list(map(int, input().split()))
q = int(input())
top_front_list = [list(map(int, input().split())) for _ in range(0, q)]

dice = Dice(face_list)
dice.all_face()
print(dice.face_all_list)
print(len(dice.face_all_list))
print(dice.face_dict)
