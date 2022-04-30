# i = 0
# c = 0
# x = int(input("輸入最大值:"))
# while i <= x:
#     c += i
#     i += 1
#     print(c)

# import random
# print(random.randint(1, 6))

# i = 1
# while i < 6:
#     i += 1
#     if i == 3:
#         break
# else:
#     print('迴圈結束')
while True:
    print('1 =蘋果汁')
    print('2 =柳橙汁')
    print('3 =葡萄汁')
    x = (input('請問你要喝啥?'))
    if x == '1':
        print('您要的商品是:蘋果汁')
    elif x == '2':
        print('您要的商品是:柳橙汁')
    elif x == '3':
        print('您要的商品是:葡萄汁')
    elif x == '4':
        break
    else:
        print('查無此商品')
