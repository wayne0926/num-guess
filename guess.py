# coding=utf-8
import random
import os
num = random.choice(range(10))
cx = int(1)
nnn = int(0)
maxnum = int(10)
minnum = int(0)
in1 = int(0)
in2 = int(0)
def fifo(aa):
    global in2
    while(aa>0):
        try:
            in2 = int(input('请猜数'))
        except ValueError:
            print('非法字符，请输入整数')
            aa = int(1)
        else:
            aa = int(0)
    return in2
while(nnn==0):#几乎没啥用
    in1 = fifo(cx)
    while in1 > num:
        if in1 <= 10:
            if in1 <=maxnum:
                maxnum = in1
            print('大了，' + str(minnum) + '到' + str(maxnum) + '之间')
            in1 = fifo(cx)
        else:
            print('超出了范围')
            in1 = fifo(cx)
    if in1 == num:
        print('恭喜!你猜中了')
        nnn = int(nnn+1)
    while in1 < num:
        if in1 >= 0:
            if in1 >=minnum:
                minnum = in1
            print('小了，' + str(minnum) + '到' + str(maxnum) + '之间')
            in1 = fifo(cx)
        else:
            print('超出了范围')
            in1 = fifo(cx)
print('正确答案是' + str(num))
os.system("pause")
