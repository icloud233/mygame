from turtle import *
def a():
    lt(90)
def d():
    rt(90)
def w():
    fd(10)
def s():
    bk(10)
def h():
    home()
def g():
    clear()
onkeypress(w,'W')
onkeypress(s,'S')
onkeypress(a,'A')
onkeypress(d,'D')
onkey(g,'G')
onkey(h,'H')
listen()
def t():
    circle(100)
def y():
    fillcolor('red')
    begin_fill()
    circle(100)
    end_fill()
def u():
    fillcolor('yellow')
    begin_fill()
    circle(100)
    end_fill()
def i():
    fillcolor('green')
    begin_fill()
    circle(100)
    end_fill()
onkey(t,'T')
onkey(y,'Y')
onkey(u,'U')
onkey(i,'I')
listen()
def z():
    shape('circle')
def x():
    shape('square')
def c():
    shape('classic')
onkey(z,'Z')
onkey(x,'X')
onkey(c,'C')
listen()
