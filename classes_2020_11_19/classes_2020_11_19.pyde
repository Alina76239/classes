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
def mode_1():
    global pos
    ellipseMode(CENTER)
    background(1)
    ellipse(pos,300,40,40)
    pos=(pos+1)%601
def mode_2():
    global pos
    ellipseMode(CENTER)
    background(1)
    ellipse(300,pos,40,40)
    pos=(pos+1)%601
def mode_3():
    global pos,vector
    ellipseMode(CENTER)
    background(1)
    ellipse(pos,300,40,40)
    pos=(pos+vector)
    if pos==600 or pos==0:
        vector=vector*-1
def mode_4():
    global xpos,xvector,ypos,yvector
    ellipseMode(CENTER)
    background(1)
    ellipse(xpos,ypos,40,40)
    xpos=(xpos+xvector)
    ypos=(ypos+yvector)
    if xpos==600 or xpos==0:
        xvector=xvector*-1
    if ypos==600 or ypos==0:
        yvector=yvector*-1
def mode_5():
    global xpos,xvector,ypos,yvector
    ellipseMode(CENTER)
    background(1)
    ellipse(xpos,ypos,40,40)
    xpos=(xpos+xvector)
    ypos=(ypos-20*yvector+g)
    yvector=yvector-0.01
    if xpos==600 or xpos==0:
        xvector=xvector*-1
    if yvector<0 or yvector==0:
        yvector=0
    if ypos>600:
        yvector=1
    
def draw():
    if (key== '1'):
        mode_1()
    elif (key=='2'):
        mode_2()
    elif (key=='3'):
        mode_3()
    elif (key=='4'):
        mode_4()
    elif (key=='5'):
        mode_5()
    
        
