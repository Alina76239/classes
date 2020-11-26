width = 800
height = 800
nx = 6
ny = 6
total = ny*nx 
basic_size = 60
size_step = 3
type_symbol = 0 # 0 - линия, 1 - квадрат ,2 - круг

def setup():
    size(width,height)
    colorMode(HSB,360,100,100)

def draw_line(x,y,len):
    line(x,y-(len/2),x,y+(len/2))

def draw_rect(x,y,len):
    rect(x-len/2,y-len/2,len,len)
    
def draw_ellipse(x,y,len):
    ellipse(x,y,len,len)

def calc_position(i, k, nx, ny):
    x = ((k+1)*width/nx)-((width/nx)/2)
    y = ((i+1)*height/ny)-((height/ny)/2)
    return x,y


def draw_symbol(t, i, k, nx, ny, basic_size, idx):
    x, y = calc_position(i, k, nx, ny)
    part = float(idx) / float(total)
    figure_size = 1+int(basic_size*part)
    if t == 0:
        stroke(0, 83*part, 85)
        noFill()
        draw_line(x,y,figure_size)
    if t == 1:
        noStroke()
        fill(0, 83*part, 85)
        draw_rect(x,y,figure_size)
    if t == 2:
        noStroke()
        fill(0, 83*part, 85)
        draw_ellipse(x,y,figure_size)
        
def draw():
    global type_symbol
    background(0,0,5)
    figure_index = 0
    for i in range(ny):
        for k in range(nx):
            draw_symbol(type_symbol, i, k, nx, ny, basic_size, figure_index)
            figure_index += 1
    
    if frameCount % 60 == 0:
        type_symbol = (type_symbol+1) % 3 # 0, 1, 2, 0, 1, 2
    
        
