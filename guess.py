import random
num = random.choice(range(10))
nnn = int(0)
while nnn < 10:
    nn = int(10 - nnn)
    in1 = int(input('请猜数' + '(' + str(nn) + ')' ))
    nnn = nnn + int(1)
    if in1 < num:
        print('小了')
    if in1 == num:
        print('恭喜!')
        nnn = 11
    if in1 > num:
        print('大了')
print(num)
