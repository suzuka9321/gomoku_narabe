# coding:utf-8
#
#
#

import config
from turtle import *


# reachモジュールで描いた×の消去
def clean():
    clear()


def judge():
    index = reach_judge(0)
    if index != None:
        x = x_point(index[1])
        y = y_point(index[0])
        cross(x,y)
        config.width[index[0]][index[1]] = 2
    elif index == None:
        index = reach_judge(1)
        if index != None:
            x = x_point(index[1])
            y = y_point(index[0])
            cross(x,y)
            config.width[index[0]][index[1]] = 2


# --------------------------------------------------------------------
# リーチ判定（○：num_1 = 0)
#　リーチになっているか横、縦、斜めのすべてを確認
# --------------------------------------------------------------------
# リーチ判定（×：num_1 = 1）
#　リーチになっているか横、縦、斜めのすべてを確認
# -------------------------------------------------------------------
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　|  |○|　|○|○|○|  |×|  |  |　|  |○|○|　|○|○|  |×|  |  |
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　|  |  |○|○|○|○|×|　|  |  |　|  |○|○|○|　|○|  |×|  |  |
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　上のように４目のリーチを探し、空きマスの値を返す
#　
#　
#　リーチがなければNoneを返す
# -------------------------------------------------------------------

def reach_judge(num_1):
    config.pass_count = 0
    index = config.mass_num - config.mass + 1
    l = config.width

    # 横のライン
    a = b = c = d = e = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(index):
            x = l[a][A],l[b][A+1],l[c][A+2],l[d][A+3],l[e][A+4]
            if num_1 == 0:
                if x == (0,1,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1,1):
                    config.pass_count = 1
                    return b,A+1
                if x == (1,1,0,1,1):
                    config.pass_count = 1
                    return c,A+2
                if x == (1,1,1,0,1):
                    config.pass_count = 1
                    return d,A+3
                if x == (1,1,1,1,0):
                    config.pass_count = 1
                    return e,A+4
            if num_1 == 1:
                if x == (0,2,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2,2):
                    config.pass_count = 1
                    return b,A+1
                if x == (2,2,0,2,2):
                    config.pass_count = 1
                    return c,A+2
                if x == (2,2,2,0,2):
                    config.pass_count = 1
                    return d,A+3
                if x == (2,2,2,2,0):
                    config.pass_count = 1
                    return e,A+4
            A += 1
        plus += 1
        a = b = c = d = e = plus

    # 縦のライン
    A = B = C = D = E = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count ==1:
            break
        a = 0
        for u in range(index):
            x = l[a][A],l[a+1][B],l[a+2][C],l[a+3][D],l[a+4][E]
            if num_1 == 0:
                if x == (0,1,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1,1):
                    config.pass_count = 1
                    return a+1,B
                if x == (1,1,0,1,1):
                    config.pass_count = 1
                    return a+2,C
                if x == (1,1,1,0,1):
                    config.pass_count = 1
                    return a+3,D
                if x == (1,1,1,1,0):
                    config.pass_count = 1
                    return a+4,E
            if num_1 == 1:
                if x == (0,2,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2,2):
                    config.pass_count = 1
                    return a+1,B
                if x == (2,2,0,2,2):
                    config.pass_count = 1
                    return a+2,C
                if x == (2,2,2,0,2):
                    config.pass_count = 1
                    return a+3,D
                if x == (2,2,2,2,0):
                    config.pass_count = 1
                    return a+4,E
            a += 1
        plus += 1
        A = B = C = D = E = plus

    # 右斜め、左から角までのライン
    A = 0
    n = 1
    for i in range(index):
        if config.pass_count ==1:
            break
        a = 0
        for u in range(n):
            x = l[a][A+4],l[a+1][A+3],l[a+2][A+2],l[a+3][A+1],l[a+4][A]
            if num_1 == 0:
                if x == (0,1,1,1,1):
                    config.pass_count = 1
                    return a,A+4
                if x == (1,0,1,1,1):
                    config.pass_count = 1
                    return a+1,A+3
                if x == (1,1,0,1,1):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (1,1,1,0,1):
                    config.pass_count = 1
                    return a+3,A+1
                if x == (1,1,1,1,0):
                    config.pass_count = 1
                    return a+4,A
            if num_1 == 1:
                if x == (0,2,2,2,2):
                    config.pass_count = 1
                    return a,A+4
                if x == (2,0,2,2,2):
                    config.pass_count = 1
                    return a+1,A+3
                if x == (2,2,0,2,2):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (2,2,2,0,2):
                    config.pass_count = 1
                    return a+3,A+1
                if x == (2,2,2,2,0):
                    config.pass_count = 1
                    return a+4,A
            a += 1
            A -= 1
        n += 1
        A = a

    # 右斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-1):
        if config.pass_count ==1:
            break
        A = index - 1
        for u in range(n):
            x = l[a][A+4],l[a+1][A+3],l[a+2][A+2],l[a+3][A+1],l[a+4][A]
            if num_1 == 0:
                if x == (0,1,1,1,1):
                    config.pass_count = 1
                    return a,A+4
                if x == (1,0,1,1,1):
                    config.pass_count = 1
                    return a+1,A+3
                if x == (1,1,0,1,1):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (1,1,1,0,1):
                    config.pass_count = 1
                    return a+3,A+1
                if x == (1,1,1,1,0):
                    config.pass_count = 1
                    return a+4,A
            if num_1 == 1:
                if x == (0,2,2,2,2):
                    config.pass_count = 1
                    return a,A+4
                if x == (2,0,2,2,2):
                    config.pass_count = 1
                    return a+1,A+3
                if x == (2,2,0,2,2):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (2,2,2,0,2):
                    config.pass_count = 1
                    return a+3,A+1
                if x == (2,2,2,2,0):
                    config.pass_count = 1
                    return a+4,A
            a += 1
            A -= 1
        n -= 1
        a = A + 2

    # 左斜め、右から角までのライン
    A = index - 1
    n = 1
    for i in range(index):
        if config.pass_count ==1:
            break
        a = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1],l[a+2][A+2],l[a+3][A+3],l[a+4][A+4]
            if num_1 == 0:
                if x == (0,1,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0,1,1):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (1,1,1,0,1):
                    config.pass_count = 1
                    return a+3,A+3
                if x == (1,1,1,1,0):
                    config.pass_count = 1
                    return a+4,A+4
            if num_1 == 1:
                if x == (0,2,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0,2,2):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (2,2,2,0,2):
                    config.pass_count = 1
                    return a+3,A+3
                if x == (2,2,2,2,0):
                    config.pass_count = 1
                    return a+4,A+4
            a += 1
            A += 1
        A = index - 1 - n
        n += 1

    # 左斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-1):
        if config.pass_count ==1:
            break
        A = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1],l[a+2][A+2],l[a+3][A+3],l[a+4][A+4]
            if num_1 == 0:
                if x == (0,1,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0,1,1):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (1,1,1,0,1):
                    config.pass_count = 1
                    return a+3,A+3
                if x == (1,1,1,1,0):
                    config.pass_count = 1
                    return a+4,A+4
            if num_1 == 1:
                if x == (0,2,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0,2,2):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (2,2,2,0,2):
                    config.pass_count = 1
                    return a+3,A+3
                if x == (2,2,2,2,0):
                    config.pass_count = 1
                    return a+4,A+4
            a += 1
            A += 1
        n -= 1
        a -= n



#x値、ｙ値を引数に該当箇所に×を描く
def cross(x,y):
    penup()
    goto(x,y)
    num = heading()
    right(num)
    penup()
    forward(config.mass_size // 2)
    pendown()
    left(135)
    forward(config.mass_size * 1.4)
    right(135)
    penup()
    forward(config.mass_size)
    pendown()
    right(135)
    forward(config.mass_size * 1.4)


# 縦位置の数値を引数に、該当箇所のｘ値を返す
def x_point(index):
    point = -config.xy + config.mass_size // 2
    for i in range(index):
        point += config.mass_size
    return point

# 横位置の数値を引数に、該当箇所のｙ値を返す
def y_point(index):
    point = config.xy - config.mass_size
    for i in range(index):
        point -= config.mass_size
    return point

