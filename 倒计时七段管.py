#SevenDigitsDrawV2.py

import turtle, time

def drawGap():

    turtle.penup()

    turtle.fd(5)

def drawLine(draw):  #绘制单段数码管

    drawGap()

    turtle.pendown() if draw else turtle.penup()

    turtle.fd(40)

    drawGap()

    turtle.right(90)

def drawDigit(digit):

    #下半部分的4段数码管

    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)

    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)

    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)

    drawLine(True) if digit in [0,2,6,8] else drawLine(False)

    turtle.left(90)  #在起点把箭头方向调整到向上

    #上半部分的3段数码管

    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)

    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)

    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)

    turtle.clear()

    turtle.pu()

    turtle.fd(40)

    turtle.pd()

    turtle.right(180)

def drawNum(num):

    turtle.pencolor('red')

    for i in range(num, -1, -1):

        drawDigit(i)
            
def main():

    turtle.setup(800, 350, 200, 200)

    turtle.penup()

    turtle.fd(-300)

    turtle.pensize(5)

    drawNum(10)

    turtle.hideturtle()

    turtle.done()

main()
