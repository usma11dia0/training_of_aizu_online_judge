n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))

cnt_gen = (t for s in S for t in T if s == t)

print(len(set(cnt_gen)))
