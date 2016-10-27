import sys
#from collections import defaultdict




def adj(size, pc):
    result = []
    
    if pc[0]+1 < size+1:
        result.append((pc[0]+1, pc[1]))
    if pc[0]-1 >= 1:
        result.append((pc[0]-1, pc[1]))
    if pc[1]+1 < size+1:
        result.append((pc[0], pc[1]+1))
    if pc[1]-1 >= 1:
        result.append((pc[0], pc[1]-1))
    
    return result

    
    
    


sin = list(sys.stdin)
size = int(sin[0])
sin = sin[1:]

i = 0
di = dict()
group = 0
notFind = True
while int(sin[i].split()[0]) != -1 and notFind:
    pc = tuple(int(item) for item in sin[i].split())
    temp = []
    for n in adj(size, pc):
        if n in di:
            temp.append(di[n])
    if len(temp) == 1:
        di[pc] = temp[0]
    elif len(temp) == 0:
        di[pc] = group
        group += 1
    else:
        
        flag = temp[0]
        
        for k in di.keys():
            if di[k] in temp[1:]:
                di[k] = flag
        
        di[pc] = flag
                
         
    #print(di)
    
    set1 = set()
    setn = set()
    for k in di.keys():
        if k[0] == 1:
            set1.add(di[k])
        elif k[0] == size:
            setn.add(di[k])

    
    if len(set1.intersection(setn)) != 0:
        notFind = False
        print i+1
        
        
        

            
            
    i += 1
    
if notFind:
    print -1

