#冒險初始能力:
#  初始血量:10點
#  初始錢:0元
#  冒險者攻擊力:1-3點
#  怪物攻擊力:1點

#冒險事件1  補血:
#  獲得紅色藥水

#冒險事件2  獲得金幣:
#  獲得金幣10-30

#冒險事件3  戰鬥:
#  擊敗怪物獲得10-20元
#  回合制，冒險者有先攻擊的優先權
#  冒險者隨機對怪物產生1-3點的傷害
#  怪物生命隨機2-10點，攻擊力1點
#  戰鬥結束，更新冒險者狀態:
#    status[0] = 1活著，0死亡
#    status[1] = 剩餘生命
#    status[2] = 剩餘金幣

import random
import time


def update_life(s):
    HP = random.randint(1, 3)
    print('角色獲得{}點HP'.format(HP))
    s[1] += HP


def update_money(s):
    MONEY = random.randint(10, 30)
    print('角色獲得{}元'.format(MONEY))
    s[2] += MONEY


def fighting(s):
    pass


status = [1, 10, 0]
event = [update_life, update_money, fighting]

while True:
    ans = input('是否繼續?')
    if (ans == 'y'):
        event[random.randrange(0, len(event))](status)
        print("目前角色狀態:HP={},Money={}".format(status[1], status[2]))
    else:
        print('881')
        break
