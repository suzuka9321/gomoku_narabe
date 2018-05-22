# coding:utf-8
#
#
#

import config
from turtle import *
from random import randrange



# cpuモジュールで描いた×の消去
def clean():
    clear()

speed(0)

def turn():
    # ＣＰＵ（×）がリーチのときビンゴする
    # プレイヤー（○）がリーチのとき阻止
    turn_1()
    if config.pass_count == 0:
        # プレイヤー（○）が３目並べているとき阻止
        # ＣＰＵ（×）が３目並べているとき４目にする
        turn_2()
        if config.pass_count == 0:
            # プレイヤー（○）が２目並べているとき阻止
            # ＣＰＵ（×）が２目並べているとき３目にする
            turn_3()
            if config.pass_count == 0:
                # プレイヤー（○）の１目の隣に置く
                # ＣＰＵ（×）の１目の隣に置く
                turn_4()
                if config.pass_count == 0:
                    # 空いているマスにランダムに×を置く
                    turn_5()


# ＣＰＵ（×）がリーチのときビンゴする
# プレイヤー（○）がリーチのとき阻止
def turn_1():
    index = judge_5(1)
    if index != None:
        x = x_point(index[1])
        y = y_point(index[0])
        cross(x,y)
        config.width[index[0]][index[1]] = 2
        config.pass_count = 1
    elif index == None:
        index = judge_5(0)
        if index != None:
            x = x_point(index[1])
            y = y_point(index[0])
            cross(x,y)
            config.width[index[0]][index[1]] = 2
            config.pass_count = 1


# プレイヤー（○）が３目並べているとき阻止
# ＣＰＵ（×）が３目並べているとき４目にする
def turn_2():
    index = judge_4(0)
    if index != None:
        x = x_point(index[1])
        y = y_point(index[0])
        cross(x,y)
        config.width[index[0]][index[1]] = 2
        config.pass_count = 1
    elif index == None:
        index = judge_4(1)
        if index != None:
            x = x_point(index[1])
            y = y_point(index[0])
            cross(x,y)
            config.width[index[0]][index[1]] = 2
            config.pass_count = 1


# プレイヤー（○）が２目並べているとき阻止
# ＣＰＵ（×）が２目並べているとき３目にする
def turn_3():
    index = judge_3(0)
    if index != None:
        x = x_point(index[1])
        y = y_point(index[0])
        cross(x,y)
        config.width[index[0]][index[1]] = 2
        config.pass_count = 1
    elif index == None:
        index = judge_3(1)
        if index != None:
            x = x_point(index[1])
            y = y_point(index[0])
            cross(x,y)
            config.width[index[0]][index[1]] = 2
            config.pass_count = 1


# プレイヤー（○）の１目の隣に置く
# ＣＰＵ（×）の１目の隣に置く
def turn_4():
    index = judge_2(0)
    if index != None:
        x = x_point(index[1])
        y = y_point(index[0])
        cross(x,y)
        config.width[index[0]][index[1]] = 2
        config.pass_count = 1
    elif index == None:
        index = judge_2(1)
        if index != None:
            x = x_point(index[1])
            y = y_point(index[0])
            cross(x,y)
            config.width[index[0]][index[1]] = 2
            config.pass_count = 1


# 空いているマスにランダムに×
def turn_5():
    while config.pass_count == 0:
        index_1 = randrange(config.mass_num)
        index_2 = randrange(config.mass_num)
        if config.width[index_1][index_2] == 0:
            config.pass_count = 1

    x = x_point(index_2)
    y = y_point(index_1)
    cross(x,y)
    config.width[index_1][index_2] = 2
        


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

def judge_5(num_1):
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



# --------------------------------------------------------------------
# ４目判定（○：num_1 = 0)
#　４目になっているか横、縦、斜めのすべてを確認
# --------------------------------------------------------------------
# ４目判定（×：num_1 = 1）
#　４目になっているか横、縦、斜めのすべてを確認
# -------------------------------------------------------------------
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　|  |○|　|○|○|  |  |×|  |  |　|  |  |○|　|○|○|  |×|  |  |
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　|  |  |  |○|○|○|×|　|  |  |　|  |  |○|○|　|○|  |×|  |  |
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　上のように４目を探し、空きマスの値を返す
#　
#　
#　４目がなければNoneを返す
# -------------------------------------------------------------------

def judge_4(num_1):
    config.pass_count = 0
    index = config.mass_num - config.mass + 2
    l = config.width

    # 横のライン
    a = b = c = d = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(index):
            x = l[a][A],l[b][A+1],l[c][A+2],l[d][A+3]
            if num_1 == 0:
                if x == (0,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1):
                    config.pass_count = 1
                    return b,A+1
                if x == (1,1,0,1):
                    config.pass_count = 1
                    return c,A+2
                if x == (1,1,1,0):
                    config.pass_count = 1
                    return d,A+3
            if num_1 == 1:
                if x == (0,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2):
                    config.pass_count = 1
                    return b,A+1
                if x == (2,2,0,2):
                    config.pass_count = 1
                    return c,A+2
                if x == (2,2,2,0):
                    config.pass_count = 1
                    return d,A+3
            A += 1
        plus += 1
        a = b = c = d = plus

    # 縦のライン
    A = B = C = D = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(index):
            x = l[a][A],l[a+1][B],l[a+2][C],l[a+3][D]
            if num_1 == 0:
                if x == (0,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1):
                    config.pass_count = 1
                    return a+1,B
                if x == (1,1,0,1):
                    config.pass_count = 1
                    return a+2,C
                if x == (1,1,1,0):
                    config.pass_count = 1
                    return a+3,D
            if num_1 == 1:
                if x == (0,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2):
                    config.pass_count = 1
                    return a+1,B
                if x == (2,2,0,2):
                    config.pass_count = 1
                    return a+2,C
                if x == (2,2,2,0):
                    config.pass_count = 1
                    return a+3,D
            a += 1
        plus += 1
        A = B = C = D = plus

    # 右斜め、左から角までのライン
    A = 1
    n = 2
    for i in range(index-1):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(n):
            x = l[a][A+3],l[a+1][A+2],l[a+2][A+1],l[a+3][A]
            if num_1 == 0:
                if x == (0,1,1,1):
                    config.pass_count = 1
                    return a,A+3
                if x == (1,0,1,1):
                    config.pass_count = 1
                    return a+1,A+2
                if x == (1,1,0,1):
                    config.pass_count = 1
                    return a+2,A+1
                if x == (1,1,1,0):
                    config.pass_count = 1
                    return a+3,A
            if num_1 == 1:
                if x == (0,2,2,2):
                    config.pass_count = 1
                    return a,A+3
                if x == (2,0,2,2):
                    config.pass_count = 1
                    return a+1,A+2
                if x == (2,2,0,2):
                    config.pass_count = 1
                    return a+2,A+1
                if x == (2,2,2,0):
                    config.pass_count = 1
                    return a+3,A
            a += 1
            A -= 1
        n += 1
        A = a

    # 右斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-2):
        if config.pass_count == 1:
            break
        A = index - 1
        for u in range(n):
            x = l[a][A+3],l[a+1][A+2],l[a+2][A+1],l[a+3][A]
            if num_1 == 0:
                if x == (0,1,1,1):
                    config.pass_count = 1
                    return a,A+3
                if x == (1,0,1,1):
                    config.pass_count = 1
                    return a+1,A+2
                if x == (1,1,0,1):
                    config.pass_count = 1
                    return a+2,A+1
                if x == (1,1,1,0):
                    config.pass_count = 1
                    return a+3,A
            if num_1 == 1:
                if x == (0,2,2,2):
                    config.pass_count = 1
                    return a,A+3
                if x == (2,0,2,2):
                    config.pass_count = 1
                    return a+1,A+2
                if x == (2,2,0,2):
                    config.pass_count = 1
                    return a+2,A+1
                if x == (2,2,2,0):
                    config.pass_count = 1
                    return a+3,A
            a += 1
            A -= 1
        n -= 1
        a = A + 2

    # 左斜め、右から角までのライン
    A = config.mass
    n = 2
    for i in range(index-1):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1],l[a+2][A+2],l[a+3][A+3]
            if num_1 == 0:
                if x == (0,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0,1):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (1,1,1,0):
                    config.pass_count = 1
                    return a+3,A+3
            if num_1 == 1:
                if x == (0,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0,2):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (2,2,2,0):
                    config.pass_count = 1
                    return a+3,A+3
            a += 1
            A += 1
        A = index - 1 - n
        n += 1

    # 左斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-2):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1],l[a+2][A+2],l[a+3][A+3]
            if num_1 == 0:
                if x == (0,1,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0,1):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (1,1,1,0):
                    config.pass_count = 1
                    return a+3,A+3
            if num_1 == 1:
                if x == (0,2,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0,2):
                    config.pass_count = 1
                    return a+2,A+2
                if x == (2,2,2,0):
                    config.pass_count = 1
                    return a+3,A+3
            a += 1
            A += 1
        n -= 1
        a -= n


# --------------------------------------------------------------------
# ３目判定（○：num_1 = 0)
#　３目になっているか横、縦、斜めのすべてを確認
# --------------------------------------------------------------------
# ３目判定（×：num_1 = 1）
#　３目になっているか横、縦、斜めのすべてを確認
# -------------------------------------------------------------------
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　|  |　|　|○|○|  |  |×|  |  |　|  |  |○|　|○|　|  |×|  |  |
#   --+--+--+--+--+--+--+--+--+--    --+--+--+--+--+--+--+--+--+--
#　上のように３目を探し、空きマスの値を返す
#　
#　
#　３目がなければNoneを返す
# -------------------------------------------------------------------

def judge_3(num_1):
    config.pass_count = 0
    index = config.mass_num - config.mass + 3
    l = config.width

    # 横のライン
    a = b = c = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(index):
            x = l[a][A],l[b][A+1],l[c][A+2]
            if num_1 == 0:
                if x == (0,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1):
                    config.pass_count = 1
                    return b,A+1
                if x == (1,1,0):
                    config.pass_count = 1
                    return c,A+2
            if num_1 == 1:
                if x == (0,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2):
                    config.pass_count = 1
                    return b,A+1
                if x == (2,2,0):
                    config.pass_count = 1
                    return c,A+2
            A += 1
        plus += 1
        a = b = c = plus

    # 縦のライン
    A = B = C = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(index):
            x = l[a][A],l[a+1][B],l[a+2][C]
            if num_1 == 0:
                if x == (0,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1):
                    config.pass_count = 1
                    return a+1,B
                if x == (1,1,0):
                    config.pass_count = 1
                    return a+2,C
            if num_1 == 1:
                if x == (0,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2):
                    config.pass_count = 1
                    return a+1,B
                if x == (2,2,0):
                    config.pass_count = 1
                    return a+2,C
            a += 1
        plus += 1
        A = B = C = plus

    # 右斜め、左から角までのライン
    A = 2
    n = 3
    for i in range(index-2):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(n):
            x = l[a][A+2],l[a+1][A+1],l[a+2][A]
            if num_1 == 0:
                if x == (0,1,1):
                    config.pass_count = 1
                    return a,A+2
                if x == (1,0,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0):
                    config.pass_count = 1
                    return a+2,A
            if num_1 == 1:
                if x == (0,2,2):
                    config.pass_count = 1
                    return a,A+2
                if x == (2,0,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0):
                    config.pass_count = 1
                    return a+2,A
            a += 1
            A -= 1
        n += 1
        A = a

    # 右斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-3):
        if config.pass_count == 1:
            break
        A = index - 1
        for u in range(n):
            x = l[a][A+2],l[a+1][A+1],l[a+2][A]
            if num_1 == 0:
                if x == (0,1,1):
                    config.pass_count = 1
                    return a,A+2
                if x == (1,0,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0):
                    config.pass_count = 1
                    return a+2,A
            if num_1 == 1:
                if x == (0,2,2):
                    config.pass_count = 1
                    return a,A+2
                if x == (2,0,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0):
                    config.pass_count = 1
                    return a+2,A
            a += 1
            A -= 1
        n -= 1
        a = A + 2

    # 左斜め、右から角までのライン
    A = config.mass
    n = 3
    for i in range(index-2):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1],l[a+2][A+2]
            if num_1 == 0:
                if x == (0,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0):
                    config.pass_count = 1
                    return a+2,A+2
            if num_1 == 1:
                if x == (0,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0):
                    config.pass_count = 1
                    return a+2,A+2
            a += 1
            A += 1
        A = index - 1 - n
        n += 1

    # 左斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-3):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1],l[a+2][A+2]
            if num_1 == 0:
                if x == (0,1,1):
                    config.pass_count = 1
                    return a,A
                if x == (1,0,1):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (1,1,0):
                    config.pass_count = 1
                    return a+2,A+2
            if num_1 == 1:
                if x == (0,2,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0,2):
                    config.pass_count = 1
                    return a+1,A+1
                if x == (2,2,0):
                    config.pass_count = 1
                    return a+2,A+2
            a += 1
            A += 1
        n -= 1
        a -= n


# --------------------------------------------------------------------
# ２目判定（○：num_1 = 0)
#　２目になっているか横、縦、斜めのすべてを確認
# --------------------------------------------------------------------
# ２目判定（×：num_1 = 1）
#　２目になっているか横、縦、斜めのすべてを確認
# -------------------------------------------------------------------
#   --+--+--+--+--+--+--+--+--+--  
#　|  |　|　|○|　|  |  |×|  |  |
#   --+--+--+--+--+--+--+--+--+--
#　上のように２目を探し、空きマスの値を返す
#　
#　
#　２目がなければNoneを返す
# -------------------------------------------------------------------

def judge_2(num_1):
    config.pass_count = 0
    index = config.mass_num - config.mass + 4
    l = config.width

    # 横のライン
    a = b = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(index):
            x = l[a][A],l[b][A+1]
            if num_1 == 0:
                if x == (0,1):
                    config.pass_count = 1
                    return a,A
            if num_1 == 1:
                if x == (0,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0):
                    config.pass_count = 1
                    return b,A+1
            A += 1
        plus += 1
        a = b = plus

    # 縦のライン
    A = B = 0
    plus = 0
    for i in range(config.mass_num):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(index):
            x = l[a][A],l[a+1][B]
            if num_1 == 0:
                if x == (0,1):
                    config.pass_count = 1
                    return a,A
            if num_1 == 1:
                if x == (0,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0):
                    config.pass_count = 1
                    return a+1,B
            a += 1
        plus += 1
        A = B = plus

    # 右斜め、左から角までのライン
    A = 3
    n = 4
    for i in range(index-3):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(n):
            x = l[a][A+1],l[a+1][A]
            if num_1 == 0:
                if x == (0,1):
                    config.pass_count = 1
                    return a,A+1
            if num_1 == 1:
                if x == (0,2):
                    config.pass_count = 1
                    return a,A+1
                if x == (2,0):
                    config.pass_count = 1
                    return a+1,A
            a += 1
            A -= 1
        n += 1
        A = a

    # 右斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-4):
        if config.pass_count == 1:
            break
        A = index - 1
        for u in range(n):
            x = l[a][A+1],l[a+1][A]
            if num_1 == 0:
                if x == (0,1):
                    config.pass_count = 1
                    return a,A+1
            if num_1 == 1:
                if x == (0,2):
                    config.pass_count = 1
                    return a,A+1
                if x == (2,0):
                    config.pass_count = 1
                    return a+1,A
            a += 1
            A -= 1
        n -= 1
        a = A + 2

    # 左斜め、右から角までのライン
    A = config.mass
    n = 4
    for i in range(index-3):
        if config.pass_count == 1:
            break
        a = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1]
            if num_1 == 0:
                if x == (0,1):
                    config.pass_count = 1
                    return a,A
            if num_1 == 1:
                if x == (0,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0):
                    config.pass_count = 1
                    return a+1,A+1
            a += 1
            A += 1
        A = index - 1 - n
        n += 1

    # 左斜め、角から下までのライン
    a = 1
    n -= 2
    for i in range(index-4):
        if config.pass_count == 1:
            break
        A = 0
        for u in range(n):
            x = l[a][A],l[a+1][A+1]
            if num_1 == 0:
                if x == (0,1):
                    config.pass_count = 1
                    return a,A
            if num_1 == 1:
                if x == (0,2):
                    config.pass_count = 1
                    return a,A
                if x == (2,0):
                    config.pass_count = 1
                    return a+1,A+1
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

