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
from tkinter import Y
from turtle import st


def update_life(s):
    HP = random.randint(1, 3)
    print('角色獲得{}點HP'.format(HP))
    s[1] += HP


def update_money(s):
    MONEY = random.randint(10, 30)
    print('角色獲得{}元'.format(MONEY))
    s[2] += MONEY


def fighting(s):
    t = 1  #attack speed
    monster_hp = random.randint(2, 10)
    print("monster_hp = %d" % monster_hp)

    while True:
        attack = random.randint(1, 3)
        print("you make damage%d" % attack)
        monster_hp -= attack
        time.sleep(t)
        print("monster_hp%d" % monster_hp)

        if (monster_hp < 1):
            print("you have defeated an enemy")
            s[2] += random.randint(10, 20)
            break
        else:
            print("you have defeated an enemy")
            s[1] -= 3
            time.sleep(t)
            print('you hurt,live=%d' % s[1])
            if (s[1] < 1):
                print("you have been defeated")
                s[0] = 0
                break


file = 'save.txt'
status = []
try:
    f = open(file, 'r')
except:
    status = [1, 10, 0]
else:
    for line in f:
        status.append(int(line))
    f.close()

print(status)

event = [update_life, update_money, fighting]

while True:
    ans = input('是否繼續?')
    if (ans == 'y'):
        event[random.randrange(0, len(event))](status)
        print("目前角色狀態:HP={},Money={}".format(status[1], status[2]))

        if status[0] == 0:
            if status[2] >= 50:
                ans = input('是否購買生藥水(50元):')
                if ans == 'y':
                    status[0] = 1
                    status[1] = 1
                    status[2] -= 50
                    for i in range(10):
                        print('復活進度:' + str(i * 10) + "%", end='\r')
                        time.sleep(0.5)
                    print("!!恭喜復活!!")
                else:
                    break
            else:
                break

    else:
        print('881')
        file = 'save.txt'
        f = open(file, 'w')
        for i in status:
            f.write(str(i) + '\n')
        f.close()
        break