# 같은 패키지에 있는 모듈은 서로 불러서 쓸 수 있음.
from RSP_Game import getStartRSPGame
from Typing_Game2 import getStartWordGame

#getStartRSPGame(4)

#getStartWordGame(3)

import turtle
t = turtle.Turtle()

def square(len):
    for i in range(4):
        t.forward(len)
        t.left(90)

def trangle(len):
    t.color("blue")
    for i in range(3):
        t.forward(len)
        t.left(90)

def circle(len):
    t.circle(len)


len = 50
while 300 > len :
    square(len)
    len += 50
