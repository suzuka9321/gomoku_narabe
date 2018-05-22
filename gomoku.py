# coding:shift-jis


#五目並べクラス
#プレイヤー対ＣＰＵ

# ○: Player
# ×: CPU

# 0: 空きマス
# 1: ○
# 2: ×






from turtle import *
import config
import reach
import cpu


class Gomoku(Turtle):
    def __init__(self):
        super(Gomoku,self).__init__()

        self.table_draw()
        onscreenclick(self.game_start)
        mainloop()


    # ゲーム画面の描画
    def table_draw(self):
        self.speed(0)
        
        # 盤面の描画
        x = y = config.xy
        for i in range(config.mass_num + 1):
            self.penup()
            self.goto(-x,y)
            self.pendown()
            self.goto(x,y)
            y -= config.mass_size
        x = y = config.xy
        for u in range(config.mass_num + 1):
            self.penup()
            self.goto(x,-y)
            self.pendown()
            self.goto(x,y)
            x -= config.mass_size

        # リセットボタンの描画
        self.penup()
        self.goto(-60,-(y+50))
        self.pendown()
        num = self.heading()
        self.right(num)
        for i in range(4):
            self.forward(120)
            self.right(90)

    # config数値のリセット
    def reset(self):
        self.reset_clear(config.width)
        config.pass_count = 0


    # ○、×記録の初期化
    def reset_clear(self,line):
        num_1 = 0
        for i in range(len(line)):
            num_2 = 0
            for u in range(len(line[num_1])):
                line[num_1][num_2] = 0
                num_2 += 1
            num_1 += 1
        


    # プレイヤーの操作を無効化
    def cpu_move(self,x,y):
        pass


    # ゲーム終了後のリセットボタン
    def game_out(self,x,y):
        if -(config.xy+170) < y < -(config.xy+50):
            if -60 < x and x < 60:
                # 盤面を消して、再び盤面の描画
                self.clear()
                cpu.clean()
                self.table_draw()

                # 履歴を初期化
                self.reset()
                onscreenclick(self.game_start)


    # クリックした位置により動作する
    # 盤面内：選択したマスに○を描画し記録する
    # 盤面外：反応しない
    # リセットボタン：盤面、記録のリセット
    # すでに○か×のマスを選択しても反応しない
    # 盤面内をクリックされるとＣＰＵのターンになる
    # プレイヤー、ＣＰＵのターンの終わりにビンゴ・引き分けの判定
    # ビンゴ・引き分けになっていれば、プレイヤー、ＣＰＵ共に操作不能になる
    # リセットボタンを押すと、再びプレイできる
    def game_start(self,x,y):
        config.pass_count = 0
        
    	# リセットボタン。○、×記録の初期化
        if -(config.xy+170) < y < -(config.xy+50):
            if -60 < x < 60:
                self.clear()
                cpu.clean()
                self.table_draw()
                self.reset()


        elif -config.xy < y < config.xy:
            if -config.xy < x < config.xy:

                # ｙ値より列の番号、○描画のｙ値を出す
                width_index = 0
                y_point = config.xy - config.mass_size
                small = config.xy - config.mass_size
                big = config.xy
                while config.pass_count == 0:
                    if small < y < big:
                        config.pass_count += 1
                    else:
                        width_index += 1
                        y_point -= config.mass_size
                    small -= config.mass_size
                    big -= config.mass_size

                # ｘ値より行の番号、○描画のｘ値を出す
                config.pass_count = 0
                length_index = 0
                x_point = -(config.xy - (config.mass_size // 2))
                small = -config.xy
                big = -(config.xy - config.mass_size)
                while config.pass_count == 0:
                    if small < x < big:
                        config.pass_count += 1
                    else:
                        length_index += 1
                        x_point += config.mass_size
                    small += config.mass_size
                    big += config.mass_size


                config.pass_count = 0
                
                # プレイヤーの手番
                if config.width[width_index][length_index] == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(x_point,y_point)
                    config.width[width_index][length_index] = 1
                    config.pass_count = 1
        
                self.gameset()
                
        # ＣＰＵの手番
        # プレイヤーの手番でconfig.pass_countが１にならないと動かない
        if config.pass_count == 1:
            config.pass_count = 0

            # ＣＰＵ（×）がリーチのときビンゴする
            # プレイヤー（○）がリーチのとき阻止
            # プレイヤー（○）が３目並べているとき阻止
            # ＣＰＵ（×）が３目並べているとき４目にする
            # プレイヤー（○）が２目並べているとき阻止
            # ＣＰＵ（×）が２目並べているとき３目にする
            # プレイヤー（○）の１目の隣に置く
            # ＣＰＵ（×）の１目の隣に置く
            # 空いているマスにランダムに×を置く
            cpu.turn()
            self.gameset()

        # ビンゴか引き分けになるとconfig.pass_countが０になり、
        # game_startに戻らない
        if config.pass_count == 1:
            onscreenclick(self.game_start)




        

    # 勝敗決定後のプレイヤー、ＣＰＵの操作無効
    def gameset(self):
        if self.judge(0,1) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("○の勝ち!!　下の枠を押して再挑戦!!")
        elif self.judge(0,32) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("×の勝ち!!　下の枠を押して再挑戦!!")
        elif self.judge(1) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("引き分け!!　下の枠を押して再挑戦!!")



    # -------------------------------------------------------------
    # 勝敗判定(num_1 = 0)
    # すべてのラインのビンゴを探る
    # 連続して並んだ五目をすべて掛け合わせ、判定する
    # num_2が1なら○、num_2が32なら×のビンゴを探す
    # ビンゴならTrueを返し、以後のラインは判定しない
    # -------------------------------------------------------------
    # 引き分け判定(num_1 = 1)
    # すべてのラインのビンゴの可能性を探る
    # 連続して並んだ五目にビンゴの可能性がなければ、count+=1 する
    # 一つの列にビンゴの可能性がなければ、judge+=1 する
    # 最後にjudgeとすべてのラインの数を比較し、同じならTrueを返す
    # -------------------------------------------------------------
    def judge(self,num_1,num_2 = None):
        pass_index = 0
        index = config.mass_num - config.mass + 1
        l = config.width
        judge = 0

        # 横のライン
        a = b = c = d = e = 0
        plus = 0
        for i in range(config.mass_num):
            if pass_index == 1:
                break
            A = 0
            count = 0
            for u in range(index):
                if num_1 == 0:
                    x = l[a][A] * l[b][A+1] * l[c][A+2] * l[d][A+3] * l[e][A+4]
                    if x == num_2:
                        pass_index = 1
                        return True
                if num_1 == 1:
                    if l[a][A] == 1 or l[b][A+1] == 1 or l[c][A+2] == 1 or l[d][A+3] == 1 or l[e][A+4] == 1:
                        if l[a][A] == 2 or l[b][A+1] == 2 or l[c][A+2] == 2 or l[d][A+3] == 2 or l[e][A+4] == 2:
                            count += 1
                    if count == index:
                        judge += 1
                A += 1
            plus += 1
            a = b = c = d = e = plus

        # 縦のライン
        A = B = C = D = E = 0
        plus = 0
        for i in range(config.mass_num):
            if pass_index == 1:
                break
            a = 0
            count = 0
            for u in range(index):
                if num_1 == 0:
                    x = l[a][A] * l[a+1][B] * l[a+2][C] * l[a+3][D] * l[a+4][E]
                    if x == num_2:
                        pass_index = 0
                        return True
                if num_1 == 1:
                    if l[a][A] == 1 or l[a+1][B] == 1 or l[a+2][C] == 1 or l[a+3][D] == 1 or l[a+4][E] == 1:
                        if l[a][A] == 2 or l[a+1][B] == 2 or l[a+2][C] == 2 or l[a+3][D] == 2 or l[a+4][E] == 2:
                            count += 1
                    if count == index:
                        judge += 1
                a += 1
            plus += 1
            A = B = C = D = E = plus

        # 右斜め、左から角までのライン
        A = 0
        n = 1
        for i in range(index):
            if pass_index == 1:
                break
            a = 0
            count = 0
            for u in range(n):
                if num_1 == 0:
                    x = l[a][A+4] * l[a+1][A+3] * l[a+2][A+2] * l[a+3][A+1] * l[a+4][A]
                    if x == num_2:
                        pass_index = 1
                        return True
                if num_1 == 1:
                    if l[a][A+4] == 1 or l[a+1][A+3] == 1 or l[a+2][A+2] == 1 or l[a+3][A+1] == 1 or l[a+4][A] == 1:
                        if l[a][A+4] == 2 or l[a+1][A+3] == 2 or l[a+2][A+2] == 2 or l[a+3][A+1] == 2 or l[a+4][A] == 2:
                            count += 1
                    if count == n:
                        judge += 1
                a += 1
                A -= 1
            n += 1
            A = a

        # 右斜め、角から下までのライン
        a = 1
        n -= 2
        for i in range(index-1):
            if pass_index == 1:
                break
            A = index - 1
            count = 0
            for u in range(n):
                if num_1 == 0:
                    x = l[a][A+4] * l[a+1][A+3] * l[a+2][A+2] * l[a+3][A+1] * l[a+4][A]
                    if x == num_2:
                        pass_index = 1
                        return True
                if num_1 == 1:
                    if l[a][A+4] == 1 or l[a+1][A+3] == 1 or l[a+2][A+2] == 1 or l[a+3][A+1] == 1 or l[a+4][A] == 1:
                        if l[a][A+4] == 2 or l[a+1][A+3] == 2 or l[a+2][A+2] == 2 or l[a+3][A+1] == 2 or l[a+4][A] == 2:
                            count += 1
                    if count == n:
                        judge += 1
                a += 1
                A -= 1
            n -= 1
            a = A + 2

        # 左斜め、右から角までのライン
        A = index - 1
        n = 1
        for i in range(index):
            if pass_index == 1:
                break
            a = 0
            count = 0
            for u in range(n):
                if num_1 == 0:
                    x = l[a][A] * l[a+1][A+1] * l[a+2][A+2] * l[a+3][A+3] * l[a+4][A+4]
                    if x == num_2:
                        pass_index = 1
                        return True
                if num_1 == 1:
                    if l[a][A] == 1 or l[a+1][A+1] == 1 or l[a+2][A+2] == 1 or l[a+3][A+3] == 1 or l[a+4][A+4] == 1:
                        if l[a][A] == 2 or l[a+1][A+1] == 2 or l[a+2][A+2] == 2 or l[a+3][A+3] == 2 or l[a+4][A+4] == 2:
                            count += 1
                    if count == n:
                        judge += 1
                a += 1
                A += 1
            A = index - 1 - n
            n += 1

        # 左斜め、角から下までのライン
        a = 1
        n -= 2
        for i in range(index-1):
            if pass_index == 1:
                break
            A = 0
            count = 0
            for u in range(n):
                if num_1 == 0:
                    x = l[a][A] * l[a+1][A+1] * l[a+2][A+2] * l[a+3][A+3] * l[a+4][A+4]
                    if x == num_2:
                        pass_index = 1
                        return True
                if num_1 == 1:
                    if l[a][A] == 1 or l[a+1][A+1] == 1 or l[a+2][A+2] == 1 or l[a+3][A+3] == 1 or l[a+4][A+4] == 1:
                        if l[a][A] == 2 or l[a+1][A+1] == 2 or l[a+2][A+2] == 2 or l[a+3][A+3] == 2 or l[a+4][A+4] == 2:
                            count += 1
                    if count == n:
                        judge += 1
                    if judge == (config.mass_num * 2) + (config.mass_num - config.mass)*2 + 2:
                        return True
                a += 1
                A += 1
            n -= 1
            a -= n
                  


    # 引数のｘ値、ｙ値の該当箇所に〇を描く
    def whole(self,x,y):
        self.penup()
        self.goto(x,y)
        num = self.heading()
        self.right(num)
        self.pendown()
        self.circle(config.mass_size // 2)



if __name__ == "__main__":
    gomoku = Gomoku()
