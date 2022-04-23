import turtle

# turtle.forward(50)  #int or float
# turtle.right(90)  #int or float turtle.Left (degree) #int or float
# turtle.forward(50)  #int or fLoat
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.done()

# for i in range(100, 5000000000000, 2):
#     print(i)

# turtle.speed(0)
# for i in range(1, 300):
#     turtle.forward(1 + i)  #int or float
#     turtle.right(90 + i * 90)
# turtle.done()

# turtle.stamp()#蓋下印章
# turtle.penup()#提筆

# turtle.color('blue')  #設定小烏龜顏色
# turtle.shape('turtle')  # 設定小烏寤形'arrow'
turtle.pensize(5)
turtle.pencolor('black')
turtle.fillcolor('yellow')
turtle.begin_fill()
for i in range(1, 6):
    turtle.forward(100)
    turtle.left(145)
turtle.end_fill()
turtle.done()