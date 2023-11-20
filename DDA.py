
def DDA(x0,y0,x1,y1):
    lst=[]
    dx=x1-x0
    dy=y1-y0
    a=(x0,y0)
    lst.append(a)
    if abs(dx)>abs(dy):
        step=abs(dx)
    else:
        step=abs(dy)
    xinc=float(dx)/step
    yinc=float(dy)/step
    j=0
    while j<step:
        x0+=xinc
        y0+=yinc
        b=(round(x0),round(y0))
        lst.append(b)
        j+=1
    for i in lst:
        print(i)
DDA(5,4,12,7)


