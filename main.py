positions = []
height = 0
width = 0
with open("test") as IN:
    y = 0
    for i in IN:
        x = 0
        for j in i:
            if j == "#":
                positions.append([x,y])
            x+=1
        width = x
        y+=1
    height = y

def sight(x1,y1,x2,y2):
    if x1 == x2:
        slope = None
    else:
        slope = (y1-y2)/(x1-x2)
    for i in positions:
        if i!=[x1,y1] and i!=[x2,y2]: 
            if slope != None and slope != 0 and x1 != i[0]:
                if (y1-i[1])/(x1-i[0]) == slope and (x2>i[0]>x1 or x2<i[0]<x2) and (y2>i[1]>y1 or y2<i[1]<y1):

                    return(0)
            elif slope == 0 and y1 == i[1] == y2:
                if x1>i[0]>x2 or x1<i[0]<x2:
                    return(0)
            elif slope == None and x1 == i[0] == x2:
                if y1>i[1]>y2 or y1<i[1]<y2:
                    return(0)
    return(1)
print(len(positions))
data = {}
Max = 0
pos = []
for i in positions:
    temp = 0
    for j in positions:
        if i!=j:
            o = sight(i[0],i[1],j[0],j[1])
            temp+=o
    if temp > Max:
        Max = temp
        pos = i

