import sys 
l = list(sys.stdin)
t = int(l[0])
index = 1

def iffivefour(lst):
    for i in range(len(lst)-4):
        if lst[i]+lst[i+1]+lst[i+2]+lst[i+3]+lst[i+4]>=4:
            return True
    return False

def ifthreetwo(lst):
    for i in range(len(lst)-2):
        if lst[i]+lst[i+1]+lst[i+2]>=2:
            return True
    return False

def getMaxLianxu(lst):
    res = 0
    local = 0
    prev = False
    for i in lst:
        if i > 0:
            local += 1
            prev = True
        elif prev:
            res = max(res, local)
            prev = False
            local = 0
    return max(res, local)

def compute(x, num, data):
    mapA2 ={2:1.880, 3:1.023,4:0.729,5:0.577, 6:0.483, 7:0.419,8:0.373, 9:0.337, 10:0.308}
    subAverage = []
    subRange = []
    index = 0
    count = 0
    while index < x:
        average = 0
        rg = [100001,-100001]
        n = num if x - index >= num else x - index
        for _ in range(n):
            i = int(data[index])
            average += i
            if i < rg[0]:
                rg[0] = i
            if i >= rg[1]:
                rg[1] = i
            index += 1
        subAverage.append(average/float(n))
        subRange.append(rg[1] - rg[0])
    numGroups = float(len(subAverage))
    
    ga = sum(subAverage)/numGroups
    gr = sum(subRange)/numGroups
    
    UCL = ga + gr * mapA2[num]
    LCL = ga - gr * mapA2[num]
    center = ga
    sigma = (UCL - center)/3
    U1 = center + 2 * sigma
    U2 = center + sigma
    L1 = center - sigma
    L2 = center - 2 * sigma
    count = [[0 for _ in range(x)] for _ in range(6)]
    index = 0
    for ele in data:
        _x = int(ele)
        if _x > UCL or _x < LCL:
            print "Out of Control"
            return
        elif UCL > _x and _x > U1:
            count[0][index] = 1
        elif U1 > _x and _x > U2:
            count[1][index] = 1
        elif U2 > _x and _x > center:
            count[2][index] = 1
        elif center > _x and _x > L1:
            count[3][index] = 1
        elif L1 > _x and _x > L2:
            count[4][index] = 1
        elif L2 > _x and _x > LCL:
            count[5][index] = 1
        index += 1
   
    if ifthreetwo(count[0]) or ifthreetwo(count[5]) :
        print "Out of Control"
        return
    
    count01 = [count[0][i] + count[1][i] for i in range(x)]
    count54 = [count[5][i] + count[4][i] for i in range(x)]
    if iffivefour(count01) or iffivefour(count54):
        print "Out of Control"
        return
    
    count012 = [count01[i] + count[2][i] for i in range(x)]
    count543 = [count54[i] + count[3][i] for i in range(x)]
    if getMaxLianxu(count012) >= 8 or getMaxLianxu(count543) >= 8:
        print "Out of Control"
        return
    print "In Control"
    return

for _ in range(t):
    info = l[index].split()
    x = int(info[0])
    n = int(info[1])
    data = info[2:]
    compute(x, n, data)
    index+=1 
