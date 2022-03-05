# 키보드로 거북이를 조종해서 그림 그리기

import turtle as t

t.title("welcome")

def turn_right():
    t.setheading(0)
    t.forward(10)


def turn_up():
    t.setheading(90) #setheading(각도)  90이면 위를 바라본다.
    t.forward(10)


def turn_left():
    t.setheading(180)
    t.forward(10)


def turn_down():
    t.setheading(270)
    t.forward(10)


def blank():
    t.clear()


t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(blank,"Escape")


t.listen()
