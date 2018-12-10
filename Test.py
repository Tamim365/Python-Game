import turtle

def sqr_multi_color(t,sz):
    for i in ["red","black","yellow","hotpink"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

wn=turtle.Screen()
wn.bgcolor('light green')

tess=turtle.Turtle()
tess.pensize(3)


size=20

for i in range(15):
    sqr_multi_color(tess ,size)
    size=size+10
    tess.forward(10)
    tess.right(10)

wn.mainloop()