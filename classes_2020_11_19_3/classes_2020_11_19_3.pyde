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
    global pos,vector
    ellipseMode(CENTER)
    background(255)
    ellipse(pos,300,40,40)
    pos=(pos+vector)
    if pos==600 or pos==0:
        vector=vector*-1
