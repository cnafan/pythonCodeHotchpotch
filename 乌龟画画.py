"""海龟画图 画出一个正方形
"""
import turtle
#t=turtle.pen()
x=input('输入间距长度：')
y=input('边的长度：')
for i in range(4):
    turtle.up()
    turtle.forward(int(x))
    turtle.down()
    turtle.forward(int(y))
    turtle.up()
    turtle.forward(int(x))
    turtle.left(90)

