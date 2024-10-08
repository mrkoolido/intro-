import pgzrun
WIDTH=500
HEIGHT=500
TITLE="welcome class"
box=Rect([70,90],(50,50))

def draw():
    screen.clear()
    screen.fill("red")
    screen.draw.line((100,20),(400,20),("black"))
    screen.draw.line((400,20),(400,400),("black"))
    screen.draw.line((400,400),(100,400),("black"))
    screen.draw.line((100,400),(100,20),("black"))
    screen.draw.circle((200,200),100,("black"))
    screen.draw.filled_circle((200,200),100,("black"))
    screen.draw.filled_rect(box,("blue"))
























pgzrun.go()