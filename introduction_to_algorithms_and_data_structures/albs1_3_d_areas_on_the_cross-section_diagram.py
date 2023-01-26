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
                # 水たまりを結合させるか否かを判定
                # 暫定で格納した水たまりの('\'インデックス, 水量)を取得
                puddle_index, puddle_water = stack_puddle.pop()
                # 導出した同一高位水量の'\'のインデックスが、水たまりの'\'のインデックスよりも小さい場合
                # 水たまりを結合し、結果をstack_puddleへ再格納。
                if start_index < puddle_index:
                    puddle_water += horizontal_water
                    # 水たまり結合後の'\'のインデックスは、同一水量の'\'を利用
                    stack_puddle.append((start_index, puddle_water))

print(stack_puddle)
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
