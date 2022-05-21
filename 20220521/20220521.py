import random

num_dice = int(input('輸入骰子數:'))
Ready = input('push any button to start')


def roll_dice(n):
    dice = []
    for i in range(n):
        dice.append(random.randint(1, 6))
    return dice


user = roll_dice(num_dice)
print('user result={}'.format(user))

comp = roll_dice(num_dice)
print('user result=%s' % comp)
