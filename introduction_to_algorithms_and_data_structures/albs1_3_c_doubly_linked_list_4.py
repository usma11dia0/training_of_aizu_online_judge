class Dice:
    # 初期サイコロの目・転がし方
    def __init__(self, top, front, right, left, back, bottom):
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
        }

    # 北に転がす
    def roll_north(self):
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
    def roll_east(self):
        self.top, self.right, self.left, self.bottom = (
            self.left,
            self.top,
            self.bottom,
            self.right,
        )

    # 西に転がす
    def roll_west(self):
        self.top, self.right, self.left, self.bottom = (
            self.right,
            self.bottom,
            self.top,
            self.left,
        )

    # 指定された方向に転がす
    def roll_dice(self, q):
        self.direction[q]()

    # 上面の数字を返す
    def show_top(self):
        return self.top


dice = list(map(int, input().split()))
d = Dice(dice[0], dice[1], dice[2], dice[3], dice[4], dice[5])

for q in input():
    d.roll_dice(q)
print(d.show_top())
