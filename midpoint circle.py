def midpoint_circle(r):
    d=1-r
    x=0
    y=r
    lst=[]
    b=(x,y)
    lst.append(b)
    while x<y:
        if d<0:#EAST
            d=d+2*x+3
            x+=1
        else:
            d=d+2*x-2*y+5 #south east 
            x+=1
            y-=1
        c=(x,y)
        lst.append(c)
    for i in lst:
        print(i)
midpoint_circle(15)