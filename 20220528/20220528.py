# def add_juice(a_list):
#     y =input("請輸入想要的果汁:")
#     if not (y in a_list):
#         a_list.append(y)
#     return a_list

# def show_juice(a_list):
#     print(a_list)
#     return a_list

# a=[]
# op={add_juice,show_juice}
# while True:
#     x=int(input('1.想加入菜單的果汁\n2.顯示菜單\n3.離開系統'))
#     if x==3:
#         print('88')
#         break
#     a= op[x-1](a)

x = int(input('x軸?'))
y = int(input('y軸?'))
import turtle


def tree_leaves(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.color('red')
    turtle.begin_fill()
    turtle.forword(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.forward(40)
    turtle.end_fill()


def tree_trunk(x, y):
    turtle.penup()
    turtle.goto(x + 12.5, y)
    turtle.pendown()
    turtle.color('green')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(15)
    turtle.right(90)
