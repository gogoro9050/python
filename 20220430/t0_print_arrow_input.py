"""
Topic:請使用input輸入要印制的箭頭大小
可利用字串乘法
e.g.
val="*" * 3
print(val)
***


1.Show:Please in row: 
2.input:3
  *  
 *** 
*****
  *  
  *  
  * 
"""

import turtle

turtle.penup()
turtle.speed(0)

for i in range(8):
    turtle.right(45 * i)
    turtle.forward(100)
    turtle.stamp()
    turtle.home()

turtle.done()
