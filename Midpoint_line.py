
def midpoint_line(x0,y0,x1,y1):
    lst=[]
    dx=x1-x0
    dy=y1-y0
    d=(2*dy)-dx
    d_e=2*dy
    d_ne=2*(dy-dx)
    a=(x0,y0)
    lst.append((a))#initial pixel
    while x0<x1:

        if d<0:#EAST
            x0 += 1
            d=d+d_e
        else:#NORTH EAST
            x0 += 1
            y0+=1
            d=d+d_ne
        b=(x0,y0)
        lst.append(b)
    print("Draw Pixel: ")
    for i in lst:
        print(i)
midpoint_line(20,10,15,28)


