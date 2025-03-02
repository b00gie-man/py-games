import turtle
t=turtle.Turtle()
t.fillcolor("white")
t.begin_fill()
for i in range(36):
    t.forward(20)
    t.right(10)
t.end_fill()


for i in range(36):
    t.forward(13)
    t.left(10)
    t.color("black")

t.up()
t.goto(45,92)
t.down()

t.circle(4)

t.up()
t.goto(-15,92)
t.down()

t.circle(4)

t.up()
t.goto(45,55)
t.down()
t.right(90)

for i in range(18):
    t.forward(5)
    t.right(11)
t.hideturtle()

turtle.done()