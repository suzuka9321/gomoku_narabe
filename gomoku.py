# coding:shift-jis


#�ܖڕ��׃N���X
#�v���C���[�΂b�o�t

# ��: Player
# �~: CPU

# 0: �󂫃}�X
# 1: ��
# 2: �~






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


    # �Q�[����ʂ̕`��
    def table_draw(self):
        self.speed(0)
        
        # �Ֆʂ̕`��
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

        # ���Z�b�g�{�^���̕`��
        self.penup()
        self.goto(-60,-(y+50))
        self.pendown()
        num = self.heading()
        self.right(num)
        for i in range(4):
            self.forward(120)
            self.right(90)

    # config���l�̃��Z�b�g
    def reset(self):
        self.reset_clear(config.width)
        config.pass_count = 0


    # ���A�~�L�^�̏�����
    def reset_clear(self,line):
        num_1 = 0
        for i in range(len(line)):
            num_2 = 0
            for u in range(len(line[num_1])):
                line[num_1][num_2] = 0
                num_2 += 1
            num_1 += 1
        


    # �v���C���[�̑���𖳌���
    def cpu_move(self,x,y):
        pass


    # �Q�[���I����̃��Z�b�g�{�^��
    def game_out(self,x,y):
        if -(config.xy+170) < y < -(config.xy+50):
            if -60 < x and x < 60:
                # �Ֆʂ������āA�ĂєՖʂ̕`��
                self.clear()
                cpu.clean()
                self.table_draw()

                # ������������
                self.reset()
                onscreenclick(self.game_start)


    # �N���b�N�����ʒu�ɂ�蓮�삷��
    # �Ֆʓ��F�I�������}�X�Ɂ���`�悵�L�^����
    # �ՖʊO�F�������Ȃ�
    # ���Z�b�g�{�^���F�ՖʁA�L�^�̃��Z�b�g
    # ���łɁ����~�̃}�X��I�����Ă��������Ȃ�
    # �Ֆʓ����N���b�N�����Ƃb�o�t�̃^�[���ɂȂ�
    # �v���C���[�A�b�o�t�̃^�[���̏I���Ƀr���S�E���������̔���
    # �r���S�E���������ɂȂ��Ă���΁A�v���C���[�A�b�o�t���ɑ���s�\�ɂȂ�
    # ���Z�b�g�{�^���������ƁA�Ăуv���C�ł���
    def game_start(self,x,y):
        config.pass_count = 0
        
    	# ���Z�b�g�{�^���B���A�~�L�^�̏�����
        if -(config.xy+170) < y < -(config.xy+50):
            if -60 < x < 60:
                self.clear()
                cpu.clean()
                self.table_draw()
                self.reset()


        elif -config.xy < y < config.xy:
            if -config.xy < x < config.xy:

                # ���l����̔ԍ��A���`��̂��l���o��
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

                # ���l���s�̔ԍ��A���`��̂��l���o��
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
                
                # �v���C���[�̎��
                if config.width[width_index][length_index] == 0:
                    onscreenclick(self.cpu_move)
                    self.whole(x_point,y_point)
                    config.width[width_index][length_index] = 1
                    config.pass_count = 1
        
                self.gameset()
                
        # �b�o�t�̎��
        # �v���C���[�̎�Ԃ�config.pass_count���P�ɂȂ�Ȃ��Ɠ����Ȃ�
        if config.pass_count == 1:
            config.pass_count = 0

            # �b�o�t�i�~�j�����[�`�̂Ƃ��r���S����
            # �v���C���[�i���j�����[�`�̂Ƃ��j�~
            # �v���C���[�i���j���R�ڕ��ׂĂ���Ƃ��j�~
            # �b�o�t�i�~�j���R�ڕ��ׂĂ���Ƃ��S�ڂɂ���
            # �v���C���[�i���j���Q�ڕ��ׂĂ���Ƃ��j�~
            # �b�o�t�i�~�j���Q�ڕ��ׂĂ���Ƃ��R�ڂɂ���
            # �v���C���[�i���j�̂P�ڂׂ̗ɒu��
            # �b�o�t�i�~�j�̂P�ڂׂ̗ɒu��
            # �󂢂Ă���}�X�Ƀ����_���Ɂ~��u��
            cpu.turn()
            self.gameset()

        # �r���S�����������ɂȂ��config.pass_count���O�ɂȂ�A
        # game_start�ɖ߂�Ȃ�
        if config.pass_count == 1:
            onscreenclick(self.game_start)




        

    # ���s�����̃v���C���[�A�b�o�t�̑��얳��
    def gameset(self):
        if self.judge(0,1) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("���̏���!!�@���̘g�������čĒ���!!")
        elif self.judge(0,32) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("�~�̏���!!�@���̘g�������čĒ���!!")
        elif self.judge(1) == True:
            onscreenclick(self.game_out)
            config.pass_count = 0
            print("��������!!�@���̘g�������čĒ���!!")



    # -------------------------------------------------------------
    # ���s����(num_1 = 0)
    # ���ׂẴ��C���̃r���S��T��
    # �A�����ĕ��񂾌ܖڂ����ׂĊ|�����킹�A���肷��
    # num_2��1�Ȃ灛�Anum_2��32�Ȃ�~�̃r���S��T��
    # �r���S�Ȃ�True��Ԃ��A�Ȍ�̃��C���͔��肵�Ȃ�
    # -------------------------------------------------------------
    # ������������(num_1 = 1)
    # ���ׂẴ��C���̃r���S�̉\����T��
    # �A�����ĕ��񂾌ܖڂɃr���S�̉\�����Ȃ���΁Acount+=1 ����
    # ��̗�Ƀr���S�̉\�����Ȃ���΁Ajudge+=1 ����
    # �Ō��judge�Ƃ��ׂẴ��C���̐����r���A�����Ȃ�True��Ԃ�
    # -------------------------------------------------------------
    def judge(self,num_1,num_2 = None):
        pass_index = 0
        index = config.mass_num - config.mass + 1
        l = config.width
        judge = 0

        # ���̃��C��
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

        # �c�̃��C��
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

        # �E�΂߁A������p�܂ł̃��C��
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

        # �E�΂߁A�p���牺�܂ł̃��C��
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

        # ���΂߁A�E����p�܂ł̃��C��
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

        # ���΂߁A�p���牺�܂ł̃��C��
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
                  


    # �����̂��l�A���l�̊Y���ӏ��ɁZ��`��
    def whole(self,x,y):
        self.penup()
        self.goto(x,y)
        num = self.heading()
        self.right(num)
        self.pendown()
        self.circle(config.mass_size // 2)



if __name__ == "__main__":
    gomoku = Gomoku()
