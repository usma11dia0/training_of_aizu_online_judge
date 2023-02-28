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
        self.face_all = [
            [self.top, self.front, self.right, self.left, self.back, self.bottom]
        ]

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
        self.face_all.extend(face_list)


dice = list(map(int, input().split()))
d = Dice(dice[0], dice[1], dice[2], dice[3], dice[4], dice[5])

n = int(input())
order_list = [list(map(int, input().split())) for _ in range(0, n)]

# N,S,W,Eに1回転ずつ。
command_roll = ["N", "S", "W", "E"]

# 右旋回を4回
command_spin = ["SR"] * 4

for cr in command_roll:
    d.roll_dice(cr)
    d.save_face()
    for cs in command_spin:
        d.roll_dice(cs)
        d.save_face()
print(d.face_all)
