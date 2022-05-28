import random

# num_dice = int(input('輸入骰子數:'))
# Ready = input('push any button to start')

# def roll_dice(n):
#     dice = []
#     for i in range(n):
#         dice.append(random.randint(1, 6))
#     return dice

# user = roll_dice(num_dice)
# print('user result={}'.format(user))

# comp = roll_dice(num_dice)
# print('user result=%s' % comp)
a = []
while True:
    x = input("1.想加入菜單的果汁\n2.顯示菜單\n3.離開系統")
    if x == "1":
        y = input("請加入果汁:")
        if not (y in a):
            a.append(y)
    elif x == "2":
        print(a)
    else:
        print('88')
        break