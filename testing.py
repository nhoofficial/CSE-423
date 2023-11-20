def midpoint_circle(r):
    d=1-r
    x=0
    y=r
    lst=[]
    a=(x,y)
    lst.append(a)
    while x<y:
        if d<0:
            d=d+2*x+3
            x+=1
            x.append()
        else:#south east
            d=d+2*x-2*y+5
            x+=1
            y+=1
        a=(x,y)
        lst.append(a)
    print(lst)

midpoint_circle(15)
