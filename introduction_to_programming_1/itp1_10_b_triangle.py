# problem: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_10_A&lang=ja

from math import sin, cos, radians

a, b, C = map(float, input().split())

# h(aを底辺とした時の高さ)を導出
h = b * sin(radians(C))

# S(面積)の導出
S = (a * h) / 2

# L(周の長さ)の導出
c = (a**2 + b**2 - 2 * a * b * cos(radians(C))) ** (1 / 2)
L = a + b + c

print(S, L, h)
