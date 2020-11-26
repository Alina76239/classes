pos=0
vector=1
xpos=50
ypos=400
xvector=1
yvector=1
g=9.8
def setup():
    size(600,600)
    frameRate(150)
    fill(150,255,0)
def draw():
    global xpos,xvector,ypos,yvector
    ellipseMode(CENTER)
    background(255)
    ellipse(xpos,ypos,40,40)
    xpos=(xpos+xvector)
    ypos=(ypos+yvector)
    if xpos==600 or xpos==0:
        xvector=xvector*-1
    if ypos==600 or ypos==0:
        yvector=yvector*-1
