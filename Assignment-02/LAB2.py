from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def find_zone(x0,y0,x1,y1):
    zone=None
    dx=x1-x0
    dy=y1-y0
    if abs(dx)>abs(dy):#zone: 0,3,4,7
        if dx>=0 and dy>=0:
            zone=0
        elif dx<=0 and dy>=0:
            zone=3
        elif dx>=0 and dy<=0:
            zone=7
        else:
            zone=4
    else:
        if dx>=0 and dy>=0:
            zone=1
        elif dx<=0 and dy>=0:
            zone=2
        elif dx>=0 and dy<=0:
            zone=6
        else:
            zone=5
    return zone

def convert_to_zone_zero(zone,x0,y0,x1,y1):
    if zone==0:
        x0,y0=x0,y0
        x1,y1=x1,y1
    elif zone==1:
        x0,y0=y0,x0
        x1,y1=y1,x1
    elif zone==2:
        x0,y0=y0,-x0
        x1,y1=y1,-x1
    elif zone==3:
        x0,y0=-x0,y0
        x1,y1=-x1,y1
    elif zone==4:
        x0,y0=-x0,-y0
        x1,y1=-x1,-y1
    elif zone==5:
        x0,y0=-y0,-x0
        x1,y1=-y1,-x1
    elif zone==6:
        x0,y0=-y0,x0
        x1,y1=-y1,x1
    elif zone==7:
        x0,y0=x0,-y0
        x1,y1=x1,-y1
    return x0,y0,x1,y1

def back_into_orginal_zone(x0,y0,a):
    if a==0:
        x0,y0=x0,y0
    elif a==1:
        x0,y0=y0,x0
    elif a==2:
        x0,y0=-y0,x0
    elif a == 3:
        x0, y0 = -x0,y0
    elif a==4:
        x0,y0=-x0,-y0
    elif a==5:
        x0,y0=-y0,-x0
    elif a==6:
        x0,y0=y0,-x0
    elif a==7:
        x0,y0=x0,-y0
    return x0,y0
def midpoint_line(x0,y0,x1,y1,k):
    dx=x1-x0
    dy=y1-y0
    d=2*dy-dx
    d_e=2*dy
    d_ne=2*(dy-dx)#initial pixel
    while x0<x1:
        x0+=1
        if d<0:#EAST
            d=d+d_e
        else:#NORTH EAST
            y0+=1
            d=d+d_ne
        x2,y2=back_into_orginal_zone(x0,y0,k)
        draw_points(x2,y2)
    #jekhane show korbe pixel

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(0,255,255) #konokichur color set (RGB)
    #call the draw methods here
    #-----------2----------------
    m = find_zone(100,300,150,300)
    x0, y0, x1, y1 = convert_to_zone_zero(m, 100,300,150,300)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(150, 300, 150, 265)
    x0, y0, x1, y1 = convert_to_zone_zero(m, 150, 300, 150, 265)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(150, 265, 100, 265)
    x0, y0, x1, y1 = convert_to_zone_zero(m, 150, 265, 100, 265)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(100, 265, 100, 230)
    x0, y0, x1, y1 = convert_to_zone_zero(m, 100, 265, 100, 230)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(100, 230, 150, 230)
    x0, y0, x1, y1 = convert_to_zone_zero(m, 100, 230, 150, 230)
    midpoint_line(x0, y0, x1, y1, m)
    #--------------2----------------
    m = find_zone(170, 300, 220, 300)#top left to right
    x0, y0, x1, y1 = convert_to_zone_zero(m, 170, 300, 220, 300)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(170, 230, 220, 230)#bottom left to right
    x0, y0, x1, y1 = convert_to_zone_zero(m, 170, 230, 220, 230)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(170, 265, 220, 265)#middle line
    x0, y0, x1, y1 = convert_to_zone_zero(m, 170, 265, 220, 265)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(170, 300, 170, 230)# left top to bottom
    x0, y0, x1, y1 = convert_to_zone_zero(m, 170, 300, 170, 230)
    midpoint_line(x0, y0, x1, y1, m)
    m = find_zone(220, 300, 220, 230)#right top to bottom
    x0, y0, x1, y1 = convert_to_zone_zero(m, 220, 300, 220, 230)
    midpoint_line(x0, y0, x1, y1, m)
    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Student ID:20101528.Lets Draw:28") #window name
glutDisplayFunc(showScreen)
glutMainLoop()