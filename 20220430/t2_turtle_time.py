"""
Topic:請使用turtle及loop及time.sleep(1)印出秒針動畫

e.g.
import time
time.sleep(1)
"""
import turtle
import time

turtle.pendown()
turtle.speed(0)

for i in range(60):
    for j in range(12):
        turtle.penup()
        turtle.right(j * 30)
        turtle.forward(100)
        turtle.stamp()
        turtle.home()
    turtle.pendown()
    turtle.right(i * 6)
    turtle.forward(100)
    turtle.home()
    time.sleep(1)
    turtle.clear()
turtle.done()
