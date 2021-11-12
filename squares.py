import turtle
a=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
col=('white','red','green','blue','yellow','magenta','purple')
a.speed(0)

for i in range (200):
    a.forward(i*4)
    a.right(91)
    a.color(col[i%7])
    for b in range(3):
        a.forward(i*4)
        a.right(91)
        for c in range(2):
            a.forward(i*4)
            a.right(91)
