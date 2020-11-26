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
    global pos
    ellipseMode(CENTER)
    background(255)
    ellipse(300,pos,40,40)
    pos=(pos+1)%601
