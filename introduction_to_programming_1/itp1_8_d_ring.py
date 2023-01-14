# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_8_D&lang=ja

import sys

# 入力データの取得
ring = str(input())
target = str(input())

# ringの文字列を2倍にする
ring_2 = ring * 2

len(target)  # 切り取り範囲
for i in range(0, len(ring)):
    cut_string = ring_2[i : i + len(target)]
    if cut_string == target:
        print("Yes")
        sys.exit(0)
print("No")
