import turtle

wn_bg=input("Input pop-up windows color: ")
tess_color=input("Input tess color: ")
pen_size=int(input("Input pen size: "))

wn=turtle.Screen()
wn.bgcolor(wn_bg)
wn.title("Hello, Tess! ")

tess=turtle.Turtle()
tess.color(tess_color)
tess.pensize(pen_size)

tess.forward(120)
tess.left(90)
tess.forward(60)
tess.left(90)
tess.forward(120)
tess.left(90)
tess.forward(60)


wn.mainloop()