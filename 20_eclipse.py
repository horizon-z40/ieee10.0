import random
import sys
import math

def ed(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def ineclipse(x,y,x1,y1,x2,y2,r):
    return ed(x,y,x1,y1) + ed(x,y,x2,y2) <= r







def insideOneOf(x,y,le):
    for e in le:
        x1, y1, x2, y2, r = [int(i) for i in e.split()]
        #print(x,y,x1,y1,x2,y2,r)
        if ineclipse(x,y,x1,y1,x2,y2,r):
            return True
    return False






sin = list(sys.stdin)[1:]


guide = True
le = []
c = 0
for i in range(len(sin)):
    if guide:
        ne = int(sin[i])
        guide = False
        e = []
    else:
        e.append(sin[i].strip())
        c += 1
        if c == ne:
            c = 0
            guide = True
            le.append(e)
            
#print(le)
                
    

    



totalEx = 16000
inside = [0]*len(le)
for i in range(totalEx):
    x = random.randrange(-5000000, 5000000)
    y = random.randrange(-5000000, 5000000)
    #print (x, y)
    x=x/100000.0
    y=y/100000.0
    
    for i in range(len(le)):
        if insideOneOf(x,y,le[i]):
            inside[i] = inside[i] + 1
            
for i in inside:
    print ""+str(int(round((1-i/float(totalEx))*100)))+"%"
            
