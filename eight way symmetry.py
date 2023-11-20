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
    lst=[]
    dx=x1-x0
    dy=y1-y0
    d=2*dy-dx
    d_e=2*dy
    d_ne=2*(dy-dx)#initial pixel
    a=(x0,y0)
    lst.append(a)
    while x0<x1:
        x0+=1
        if d<0:#EAST
            d=d+d_e
        else:#NORTH EAST
            y0+=1
            d=d+d_ne
        x2,y2=back_into_orginal_zone(x0,y0,k)
        tup=(x2,y2)
        lst.append(tup)
    for i in lst:
        print(i)
m = find_zone(-10,-20,-20,70)
x0, y0, x1, y1 = convert_to_zone_zero(m, -10,-20,-20,70)
midpoint_line(x0, y0, x1, y1, m)