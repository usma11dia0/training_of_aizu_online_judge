import sys
from collections import deque


class Dice:
    # 初期サイコロの目・転がし方
    def __init__(
        self, top: int, front: int, right: int, left: int, back: int, bottom: int
    ) -> None:
        self.top = top
        self.front = front
        self.right = right
        self.left = left
        self.back = back
        self.bottom = bottom

        self.direction = {
            "N": self.roll_north,
            "S": self.roll_south,
            "E": self.roll_east,
            "W": self.roll_west,
            "SR": self.spin_right,
        }
        self.face_all = deque()

    # 北に転がす
    def roll_north(self) -> None:
        self.top, self.front, self.back, self.bottom = (
            self.front,
            self.bottom,
            self.top,
            self.back,
        )

    # 南に転がす
    def roll_south(self):
        self.top, self.front, self.back, self.bottom = (
            self.back,
            self.top,
            self.bottom,
            self.front,
        )

    # 東に転がす
    def roll_east(self) -> None:
        self.top, self.right, self.left, self.bottom = (
            self.left,
            self.top,
            self.bottom,
            self.right,
        )

    # 西に転がす
    def roll_west(self) -> None:
        self.top, self.right, self.left, self.bottom = (
            self.right,
            self.bottom,
            self.top,
            self.left,
        )

    # 右に旋回する
    def spin_right(self) -> None:
        self.front, self.right, self.back, self.left = (
            self.left,
            self.front,
            self.right,
            self.back,
        )

    # 指定された方向に転がす
    def roll_dice(self, q) -> None:
        self.direction[q]()

    # 上面の数字を返す
    def show_top(self) -> int:
        return self.top

    # 回転後の結果を保持
    def save_face(self) -> None:
        face_list = [
            self.top,
            self.front,
            self.right,
            self.left,
            self.back,
            self.bottom,
        ]
        self.face_all.append(face_list)


def is_same_dice(dl: Dice, dr: Dice) -> bool:
    for dl_face in dl.face_all:
        for dr_face in dr.face_all:
            if dl_face == dr_face:
                return True
    return False


n = int(input())
dice_list = []
for i in range(0, n):
    dice = list(map(int, input().split()))
    d = Dice(dice[0], dice[1], dice[2], dice[3], dice[4], dice[5])
    dice_list.append(d)

# "top", "front", "right", "left", "back", "bottom"が
# それぞれ上面にくるように回転
command_roll = ["", "N", "S", "W", "E", "NN"]
command_reverse = ["", "S", "N", "E", "W", "SS"]
# 右旋回を4回
command_spin = ["SR"] * 4

for d in dice_list:
    for roll, reverse in zip(command_roll, command_reverse):
        if roll == "NN":
            d.roll_dice(roll[0])
            d.roll_dice(roll[0])
        elif roll != "":
            d.roll_dice(roll)
        for spin in command_spin:
            d.roll_dice(spin)
            d.save_face()
        if reverse == "SS":
            d.roll_dice(reverse[0])
            d.roll_dice(reverse[0])
        elif reverse != "":
            d.roll_dice(reverse)

# 結果の出力
for i in range(0, len(dice_list) - 1):
    for j in range(i + 1, len(dice_list)):
        is_same = is_same_dice(dice_list[i], dice_list[j])
        if is_same:
            print("No")
            sys.exit(0)
print("Yes")
