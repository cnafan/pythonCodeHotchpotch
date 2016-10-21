"""tkinter_test
"""
import time
from tkinter import *

def choose_color():
    """change color"""
    col=colorchooser.askcolor()
    return col
def dianjianniu(event):
    if event.keysym=='1':
        pass
def showcanvas():
    pass
def right():
    if sanjiao
    for x in range(90):
        canvas.move(sanjiao,5,0)
        tk.update()
        time.sleep(0.05)
def left():
    for x in range(90):
        canvas.move(sanjiao,0,0)
        tk.update()
        time.sleep(0.05)
def up():
    for x in range(90):
        canvas.move(sanjiao,0,5)
        tk.update()
        time.sleep(0.05)
def down():
    for x in range(90):
        canvas.move(sanjiao,0,-5)
        tk.update()
        time.sleep(0.05)
if __name__=='__main__':
    tk=Tk()
    button_up=Button(tk,text='上',command=showcanvas)
    button_f=Button(tk,text='显示图片',command=showcanvas)
    button_f.pack()
    canvas=Canvas(tk,width=500,height=500)
    canvas.create_line(15,15,480,480)
    canvas.create_line(480,15,15,480)
    canvas.create_rectangle(15,15,480,480)
    sanjiao=canvas.create_polygon(0,0,0,30,30,15)
    button_up=Button(tk,text='上',command=up)
    button_up.pack()
    button_down=Button(tk,text='下',command=down)
    button_down.pack()
    button_left=Button(tk,text='左',command=left)
    button_left.pack()
    button_right=Button(tk,text='右',command=right)
    button_right.pack()
    canvas.pack()
    bu=Button(tk,text='改变颜色',command=choose_color)
    bu.pack()

