positions = []
Height = 0
dif = 25
Width = 0
IN = loadStrings("https://raw.githubusercontent.com/JosephcatZ/day-10/master/input")
print(IN)
y = 0
for i in IN:
    x = 0
    for j in i:
        if j == "#":
            positions.append([x,y])
        x+=1
    Width = x
    y+=1
Height = y
def setup():
    size(Width*dif,Height*dif)
def sight(x1,y1,x2,y2):
    x1 = float(x1)
    x2 = float(x2)
    y1 = float(y1)
    yu2 = float(y2)
    if x1 == x2:
        slope = "None"
    else:
        slope = (y1-y2)/(x1-x2)
    for j in positions:
        i = [float(j[0]),float(j[1])]
        if i!=[x1,y1] and i!=[x2,y2]:
            if x1 == i[0]:
                nuSlope = "None"
            else:
                nuSlope = (y1-i[1])/(x1-i[0])
            if nuSlope == slope and (y1<i[1]<y2 or y1>i[1]>y2 or x1>i[0]>x2 or x1<i[0]<x2):
                return(0)
    return(1)
print(len(positions))
data = {}
Max = 0
pos = []
"""
for i in positions:
    temp = 0
    for j in positions:
        if i!=j:
            o = sight(i[0],i[1],j[0],j[1])
            temp+=o
    if temp > Max:
        Max = temp
        pos = i
"""  
t = 0  
Maxcount = 0
pos = []
Halt = False
data = "["
for i in positions:
    data += "("+str(i[0])+","+str(i[1])+"),"
data += "]"
print(data)
print(sight(0,4,0,2))
def draw():

    global t
    global Maxcount
    global pos
    global Halt
    background(0)
    X = positions[t%len(positions)][0]*dif+dif/2
    Y = positions[t%len(positions)][1]*dif+dif/2
    #X=11*dif+dif/2
    #Y = 13*dif+dif/2
    if t > len(positions):
        print(t)
        X = pos[0]*dif+dif/2
        Y = pos[1]*dif+dif/2
        if not(Halt):
            print(pos,Maxcount)
            
            Halt = True
    #X=mouseX
    #Y = mouseY
    count = 0
    for i in positions:
        
        stroke(0,255,0)
        strokeWeight(0.25)
        if (sight(X/dif,Y/dif,i[0],i[1]) == 1 and i!=[X/dif,Y/dif]):
            count += 1
            line(X,Y,i[0]*dif+dif/2,i[1]*dif+dif/2)
            fill(0,255,0)
        else:
            fill(255)
        noStroke()
        ellipse(i[0]*dif+dif/2,i[1]*dif+dif/2,2,2)
    if Maxcount<count:
        Maxcount = count
        pos = [X/dif,Y/dif]
    t+=1
    
