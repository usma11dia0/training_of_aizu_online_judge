from collections import deque

# 入力データの取得
A = str(input())

# '\'が入力される度にそのインデックスを格納するスタック
# stack_paddle = deque([’\'のインデックス])
stack_back_slash = deque()

# 水たまりを格納するスタック
# stack_paddle = deque([('\'のインデックス , 水量)])
stack_puddle = deque()

# 同じ高さの'\'と'/'の間にある同一高位の水量
horizontal_water = 0

for index, a in enumerate(A):
    if a == "\\":
        stack_back_slash.append(index)
    elif a == "/":
        if len(stack_back_slash) > 0:
            start_index = stack_back_slash.pop()
            # 同一高位の水の量 = "/"のインデックス - 直近の"\"のインデックス
            horizontal_water = index - start_index

            if len(stack_puddle) == 0:
                stack_puddle.append((start_index, horizontal_water))
            else:
                # 導出した同一高位水量の'\'のインデックスが、既出の水たまりの'\'のインデックスよりも
                # 大きくなる(右側にくる)まで、両者の結合を繰り返す
                while True:
                    # 暫定で格納した水たまりの('\'インデックス, 水量)を取得
                    puddle_index, puddle_water = stack_puddle.pop()
                    # 導出した同一高位水量の'\'のインデックスが、水たまりの'\'のインデックスよりも大きい場合
                    # stack_puddleへ格納しwhileループを終了
                    if puddle_index < start_index:
                        stack_puddle.append((puddle_index, puddle_water))
                        stack_puddle.append((start_index, horizontal_water))
                        break
                    # 導出した同一高位水量の'\'のインデックスが、水たまりの'\'のインデックスよりも小さい場合
                    # 同一高位水量と水たまりの水量を結合し、whileループを繰り返す。
                    elif start_index < puddle_index:
                        horizontal_water += puddle_water

# 結果の出力
sum_water = 0
for puddle in stack_puddle:
    sum_water += puddle[1]

print(sum_water)
print(len(stack_puddle), end=" ")

each_puddle = deque()
for puddle in stack_puddle:
    each_puddle.append(str(puddle[1]))
print(" ".join(each_puddle))
