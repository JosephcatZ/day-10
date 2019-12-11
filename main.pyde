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
t = 0  
Maxcount = 0
pos = []
bestsight = []
Halt = False
def part_1(positions):
    insight = []
    global t
    global Maxcount
    global pos
    global Halt
    global bestsight
    background(0)
    X = positions[t%len(positions)][0]*dif+dif/2
    Y = positions[t%len(positions)][1]*dif+dif/2
    #X= 27*dif+dif/2
    #Y = 19*dif+dif/2
    if t > len(positions):
        print(t)
        X = pos[0]*dif+dif/2
        Y = pos[1]*dif+dif/2
        if not(Halt):
            print(pos,Maxcount)
            
            Halt = True
            return(1)
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
            insight.append(i)
        else:
            fill(255)
        noStroke()
        ellipse(i[0]*dif+dif/2,i[1]*dif+dif/2,2,2)
    if Maxcount<count:
        Maxcount = count
        pos = [X/dif,Y/dif]
        bestsight = []
        for i in insight:
            bestsight.append(i)
    t+=1
    return(0)
p2 = 0
temp = 0
def part_2():
    insight = []
    global t
    global Maxcount
    global pos
    global positions
    global Halt
    global bestsight
    global temp
    background(0)
    #X= 27*dif+dif/2
    #Y = 19*dif+dif/2
    if positions == []:
        return(3)
    if t == 200:
        global p2
        p2 = temp
        print(temp)
    #X=mouseX
    #Y = mouseY
    count = 0
    angles = []
    Key = []
    for i in positions:
        ellipse(i[0]*dif+dif/2,i[1]*dif+dif/2,2,2)
    for i in bestsight:
        angles.append((degrees(atan2(i[1] - pos[1], i[0] - pos[0]))+90)%360)
        Key.append(i)
    temp = min(angles)
    temp = angles.index(temp)
    stroke(255,0,0)
    line(pos[0]*dif+dif/2,pos[1]*dif+dif/2,Key[temp][0]*dif+dif/2,Key[temp][1]*dif+dif/2)
    a = temp
    temp = Key[temp]
    bestsight.pop(a)
    positions.remove(temp)
    if bestsight == []:
        for i in positions:
            if (sight(X/dif,Y/dif,i[0],i[1]) == 1 and i!=[X/dif,Y/dif]):
                count += 1
                line(X,Y,i[0]*dif+dif/2,i[1]*dif+dif/2)
                fill(0,255,0)
                bestsight.append(i)
    print(t,temp)
    t+=1 
    return(2)
status = 0
def draw():
    global status
    if status == 0:
        status = part_1(positions)
    if status == 1:
        global t
        t = 0
        status = 2
    if status == 2:
        status = part_2()
    if status ==3:
        textAlign(CENTER,CENTER)
        text(">Part 1:\t"+str(Maxcount)+"\n\n>Part 2:\t"+str(p2[0]*100+p2[1]),width/2,height/2)
