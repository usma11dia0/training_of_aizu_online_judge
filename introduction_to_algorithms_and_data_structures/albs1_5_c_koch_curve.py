from math import radians, cos, sin


def create_koch_curve(n: int, p1_x: int, p1_y: int, p2_x: int, p2_y: int):

    # 1.与えられた線分(p1,p2)を3等分する　p1 s u t p2
    s_x = (p2_x * 1) / 3 + (p1_x * 2) / 3
    s_y = (p2_y * 1) / 3 + (p1_y * 2) / 3
    t_x = (p1_x * 1) / 3 + (p2_x * 2) / 3
    t_y = (p1_y * 1) / 3 + (p1_y * 2) / 3

    # 2.線分を3等分する2点s,tを頂点とする正三角形(s,u,t)を作成する
    # 点sを原点まで平行移動させ、stと90°反時計回りさせたsvの座標をそれぞれ求める
    s_t_x = t_x - s_x
    s_t_y = t_y - s_y
    s_v_x = -(t_y - s_y)
    s_v_y = t_x - s_x
    # stとsvを直交座標とみなして、stを60°反時計回りさせたsuの座標を求める
    # su = cos60*st + sin60*sv
    #    = cos60((s_t_x, s_t_y)) + sin60((s_v_x, s_v_y))
    #    = (cos60(s_t_x) + sin60(s_v_x) , cos60(s_t_y) + sin60(s_v_y))
    s_u_x = cos(radians(60)) * s_t_x + sin(radians(60)) * s_v_x
    s_u_y = cos(radians(60)) * s_t_y + sin(radians(60)) * s_v_y
    # 点sを元の位置まで平行移動させ、点uの座標を導出する
    # ou = os + su
    u_x = s_x + s_u_x
    u_y = s_y + s_u_y
    return s_x, s_y, t_x, t_y, u_x, u_y

    # 再帰処理について追記する


# 入力データの取得
n = int(input())

# 初期値の設定
p1_x, p1_y = (0, 0)
p2_x, p2_y = (100, 0)

print(create_koch_curve(1, p1_x, p1_y, p2_x, p2_y))
