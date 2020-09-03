import turtle
def drawSpiral(t,length,color,colorBase):
    if length == 0:
        return

    newColor=(int(color[1:],16)+2**10)%(2**24)
    base=int(colorBase[1:],16)

    if newColor<base:
        newColor=(newColor+base)%(2**24)

    newColor=hex(newColor)[2:]
    newColor="#"+("0"*(6-len(newColor)))+newColor
    t.color(newColor)
    t.forward(length)
    t.left(90)

    drawSpiral(t,length-1,newColor,colorBase)


def main():
    t=turtle.Turtle()
    screen=t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(-100,100)
    t.pendown()
    drawSpiral(t,200,"#000000","#ff00fff")
    screen.exitonclick()
    
if __name__=="__main__":
    main()