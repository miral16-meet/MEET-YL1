import turtle
def draw_triangle(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x+20,y+20)
    turtle.penup()
    turtle.pendown()
    turtle.goto(x+40,y+0)
    turtle.penup()
    turtle.pendown()
    turtle.goto(x+0,y+0)
    turtle.pensize(40)
    turtle.color('red', 'red')
    turtle.begin_fill()
    draw_triangle(0,0)
    turtle.end_fill()

    
def draw_circle():
    turtle.color('blue' , 'blue')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_canvas2():
    draw_circle()
    turtle.color('red', 'red')
    turtle.onscreenclick(turtle.showturtle(),btn=1,add=True)
    turtle.ondrag(turtle.goto,btn=1,add=True)

    
draw_canvas2()
def draw_canvas2():
    draw_circle()
    turtle.color('red', 'red')
    turte.onscreenclick(turtle.goto,btn=1,add=True)
    turtle.ondrag(turtle.goto,btn=1,add=True)

    
def draw_canvas2():
    draw_circle()
    turtle.color('red', 'red')
    turtle.onscreenclick(turtle.goto,btn=1,add=True)
    turtle.ondrag(turtle.goto,btn=1,add=True)

    
draw_canvas2()
def draw_canvas3():
    draw_triangle(0,0)
    turtle.color('red', 'red')
    turtle.onscreenclick(turtle.goto,btn=1,add=True)
    turtle.ondrag(turtle.goto,btn=1,add=True)

    
def draw_canvas4():
    draw_canvas2()
    draw_canvas3()

    
draw_canvas4()