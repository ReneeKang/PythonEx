import turtle as t
import random

t.shape("turtle")
t.speed(0)

for x in range(500):
    a = random.randint(1,360)
    t.setheading(a) # 거북이 방향을 a각도로 돌린다.
    b = random.randint(1,20)
    t.forward(b)
