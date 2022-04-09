print(1 + 2 * 259 * 72 * 2 / 1 / 50)
print('來玩剪刀石頭布  剪刀=1  石頭=2  布=3')
aaa = int(input("請問你出的牌:"))
if (aaa > 2):
    print("我出剪刀  you lose")
if (aaa < 2):
    print("我出石頭  you lose")
if (aaa == 2):
    print("我出布  you lose")