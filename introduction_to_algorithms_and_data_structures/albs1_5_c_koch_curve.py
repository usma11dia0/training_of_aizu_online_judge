import math


def create_koch_curve(n: int, p1_x: int, p1_y: int, p2_x: int, p2_y: int):

    # 1.与えられた線分(p1,p2)を3等分する　p1 s u t p2
    s_x = (p2_x * 1) / 3 + (p1_x * 2) / 3
    s_y = (p2_y * 1) / 3 + (p1_y * 2) / 3
    t_x = (p1_x * 1) / 3 + (p2_x * 2) / 3
    t_y = (p1_y * 1) / 3 + (p1_y * 2) / 3

    # 2.線分を3等分する2点s,tを頂点とする正三角形(s,u,t)を作成する
    # 線分stを90°反時計回りした線分svの頂点vを求める
    v_x = -t_y
    v_y = t_x
    # 線分stと線分svを直交座標とみなして線分stを60°反時計回りさせ
    # suベクトルを導出する
    # su = cos60*st + sin60*sv
    #    = cos60(ot-os) + sin60(ov-os)
    #    = cos60((t_x,t_y)-(s_x,s_y)) + sin60((v_x,v_y)-(s_x,s_y))
    #    = (cos60(t_x-s_x)+sin60(v_x-s_x), cos60(t_y-s_y)+sin60(v_y-s_y))
    u_x = math.cos(60) * (t_x - s_x) + math.sin(60) * (v_x - s_x)
    u_y = math.cos(60) * (t_y - s_y) + math.sin(60) * (v_y - s_y)

    return s_x, s_y, t_x, t_y, u_x, u_y


# 入力データの取得
n = int(input())

# 初期値の設定
p1_x, p1_y = (0, 0)
p2_x, p2_y = (100, 0)

print(create_koch_curve(1, p1_x, p1_y, p2_x, p2_y))
