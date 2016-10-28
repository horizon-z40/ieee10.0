from math import floor
import sys

def fifo( frames, cycle, data ):
    f = -1
    page_replacement = 0
    page = [-1] * frames
    
    for i in range(cycle):
        flag = 0
        for j in range(frames):
            if(page[j] == data[i]):
                flag = 1
                break
        if flag == 0:
            f = ( f + 1 )% frames
            page[f] = data[i]
            page_replacement += 1
    res = page_replacement - frames 
    if res < 0:
        return 0
    else:
        return res

def lru( frames, cycle, data ):
    x = 0
    page_replacement = 0
    page = []
    for i in range(frames):
        page.append(-1)

    for i in range(cycle):
        flag = 0
        for j in range(frames):
            if(page[j] == data[i]):
                flag = 1
                break
            
        if flag == 0:
            if page[x] != -1:
                min = 999
                for k in range(frames):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == data[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = data[i]
            x=(x+1)%frames
            page_replacement+=1
    res = page_replacement - frames 
    if res < 0:
        return 0
    else:
        return res   

sin = list(sys.stdin)[1:]
guide = True
c=0
for i in range(len(sin)):
    if guide:
        frames, pSize, cycle = sin[i].strip().split()
        frames, pSize, cycle = int(frames), int(pSize), int(cycle)
        guide = False
        data = []
    else:
        toA = floor(int(sin[i])/float(pSize))
        data.append(toA)
        c += 1
        if c == cycle:
            c = 0
            guide = True
            l = lru(frames, cycle, data )
            f = fifo(frames, cycle, data)
            if l < f:
                print("yes" + " " + str(f) + " " + str(l))
            else:
                print("no" + " " + str(f) + " " + str(l))
