from math import asin
from math import tan
from math import atan
from math import floor

#p2 must be the vertex between 1 and 3
class latlon:
    n=float()
    w=float()
    def __init__(self, north, west):
        self.n=north
        self.w=west

p1=latlon(38.893957,-92.201767)
p2=latlon(38.893953,-92.201027)
p3=latlon(38.894567,-92.201008)

p4=latlon(38.202472,-91.736857)
p5=latlon(38.203990,-91.734097)
p6=latlon(38.205077,-91.735023)


def add(p1, p2):
    north=p1.n+p2.n
    west=p1.w+p2.w
    return latlon(north,west)

def sub(p1,p2):
    north=p1.n-p2.n
    west=p1.w-p2.w
    return latlon(north,west)

def sdiv(p,scalar):
    north=p.n/scalar
    west=p.w/scalar
    return latlon(north,west)

def smult(p, scalar):
    north=p.n*scalar
    west=p.w*scalar
    return latlon(north,west)

def mag(p):
    return (p.n*p.n+p.w*p.w)**.5

def rectMission(p1, p2, p3, alt, cam, imgOvr=.05):
    camParam={'pi':{'ssizem':2.74, 'ssizep':3.76, 'flen':3.6},
              'canon':{'ssizem':5.7, 'ssizep':7.6, 'flen':5.2}}
    v21=sub(p2,p1)
    v23=sub(p3,p2)
    mainvectorangle=asin(v21.n/mag(v21))
    if mainvectorangle>0:
        bearing=90-mainvectorangle
    else:
        bearing = 270+abs(mainvectorangle)
    mdeg=110574.611
    viewangm=2*atan(camParam[cam]['ssizem']/(2*camParam[cam]['flen']))
    viewangp=2*atan(camParam[cam]['ssizep']/(2*camParam[cam]['flen']))
    innerspacing=alt*tan(viewangm)*(1-imgOvr)/mdeg
    outerspacing=alt*tan(viewangp)*(1-imgOvr)/mdeg
    innerstep=smult(sdiv(sub(p1,p2), mag(sub(p1,p2))),innerspacing)
    outerstep=smult(sdiv(sub(p3,p2), mag(sub(p3,p2))),outerspacing)
    innerlimit=floor(mag(sub(p2,p1))/mag(innerstep))
    outerlimit=floor(mag(sub(p3,p1))/mag(outerstep))

    position=add(add(p2,sdiv(outerstep,2)),sdiv(innerstep,2))
    picNum=0
    print (position.n, position.w, picNum)
    for i in range(0,int(outerlimit)):
        picNum+=1
        for k in range(0,int(innerlimit)):
            if i%2==0:
                position=add(position,innerstep)
                print (position.n, position.w, picNum)
            else:
                position=sub(position,innerstep)
                print (position.n, position.w, picNum)
            picNum+=1
        if i!= int(outerlimit-1):
            position=add(position,outerstep)
            print (position.n, position.w, picNum)
    print (position.n, position.w, picNum, outerlimit, innerlimit)

rectMission(p1,p2,p3,20, 'pi')
