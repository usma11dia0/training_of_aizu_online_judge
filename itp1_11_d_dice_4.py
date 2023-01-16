# さいころの各変数の意味
# top：上の面
# front：手前の面
# right: 右の面
# left: 左の面
# back：奥の面
# bottom：下の面

from typing import Type
import sys

# classの定義
class Dice:
    # 初期値
    face_name = ["top", "front", "right", "left", "back", "bottom"]

    # roll関連変数
    # 変更対象の面(縦)
    roll_vertical = ["top", "front", "bottom", "back"]
    # 回転後の面(縦)
    roll_to_n = ["front", "bottom", "back", "top"]  # ひとつ左にずれる
    roll_to_s = ["back", "top", "front", "bottom"]  # ひとつ右にずれる
    # 変更対象の面(横)
    roll_horizontal = ["top", "right", "bottom", "left"]
    # 回転後の面(横)
    roll_to_w = ["right", "bottom", "left", "top"]  # ひとつ左にずれる
    roll_to_e = ["left", "top", "right", "bottom"]  # ひとつ右にずれる

    # spin関連変数
    # 変更対象の面(旋回)
    spin_right = ["front", "right", "back", "left"]
    # 旋回後の面(右)
    spin_to_r = ["left", "front", "right", "back"]  # ひとつ右にずれる

    def __init__(self, face_list: list, face_name: list = face_name) -> None:
        self.face_dict = dict(zip(face_name, face_list))
        self.face_dict_all = []
        self.face_dict_all_top = []

    def roll(
        self,
        orders: str,
        roll_vertical: list = roll_vertical,
        roll_horizontal: list = roll_horizontal,
        roll_to_n: list = roll_to_n,
        roll_to_s: list = roll_to_s,
        roll_to_e: list = roll_to_e,
        roll_to_w: list = roll_to_w,
    ) -> dict:
        for order in orders:
            # 値渡しで辞書型をコピーする
            current_face_dict = self.face_dict.copy()
            # 縦回転(上方向)
            if order == "N":
                for target_face, change_face in zip(roll_vertical, roll_to_n):
                    self.face_dict[target_face] = current_face_dict[change_face]
            # 縦回転(下方向)
            elif order == "S":
                for target_face, change_face in zip(roll_vertical, roll_to_s):
                    self.face_dict[target_face] = current_face_dict[change_face]
            # 横回転(右方向)
            elif order == "E":
                for target_face, change_face in zip(roll_horizontal, roll_to_e):
                    self.face_dict[target_face] = current_face_dict[change_face]
            # 横回転(左方向)
            elif order == "W":
                for target_face, change_face in zip(roll_horizontal, roll_to_w):
                    self.face_dict[target_face] = current_face_dict[change_face]
        return self.face_dict

    def spin_right(
        self, orders: str, spin_right: list = spin_right, spin_to_r: list = spin_to_r
    ) -> dict:
        for order in orders:
            # 値渡しで辞書型をコピーする
            current_face_dict = self.face_dict.copy()
            # 旋回 (右方向)
            if order == "R":
                for target_face, change_face in zip(spin_right, spin_to_r):
                    self.face_dict[target_face] = current_face_dict[change_face]
        return self.face_dict

    # 24通り全ての組み合わせを列挙
    def face_all(self) -> None:
        # 1. topが1,2,3,4,5,6になる組み合わせを列挙
        # 初期状態を取得 (topが1)
        current_face_dict = self.face_dict.copy()
        self.face_dict_all_top.append(current_face_dict)

        # それぞれ一回ずつ'NSWE','EE'に回転 (topが2,3,4,5と6)
        for s in ["N", "S", "W", "E", "EE"]:
            self.face_dict = current_face_dict.copy()
            self.face_dict_all_top.append(self.roll(s))

        # 2. topを軸として右旋回を4回繰り返す。
        for face_dict_top in self.face_dict_all_top:
            for s in ["R", "RR", "RRR", "RRRR"]:
                self.face_dict = face_dict_top.copy()
                self.face_dict_all.append(self.spin_right(s))

    def top_face(self):
        return self.face_dict["top"]

    def right_face(self, top: int, front: int):
        for face_dict in self.face_dict_all:
            if (face_dict["top"] == top) and (face_dict["front"] == front):
                return face_dict["right"]


# 関数定義
def is_same_dice(dice_1: Type[Dice], dice_2: Type[Dice]) -> str:
    for dice_1_face_dict in dice_1.face_dict_all:
        for dice_2_face_dict in dice_2.face_dict_all:
            if dice_1_face_dict == dice_2_face_dict:
                return "Yes"
    return "No"


# 入力データの取得
n = int(input())
dice_face_list = [list(map(int, input().split())) for _ in range(0, n)]

dice_list = []
for dice_face in dice_face_list:
    dice = Dice(dice_face)
    dice_list.append(dice)

# diceの面の組み合わせを全列挙
for dice in dice_list:
    dice.face_all()

for i in range(0, len(dice_list) - 1):
    for j in range(i + 1, len(dice_list)):
        result = is_same_dice(dice_list[i], dice_list[j])
        if result == "Yes":
            print("No")
            sys.exit(0)
print("Yes")
