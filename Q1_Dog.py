import sys

def dog_walker(l, n):
    t1 = sorted(l)
    iv = []
    for i in range(1,len(t1)):
        iv.append(t1[i]-t1[i-1])
    iv2 = sorted(iv)
    
    todelete = n-1
    return sum(iv2[:len(iv2)-todelete])


l = list(sys.stdin)

guide = True

c = 0
for i in range(len(l)):
    
    if guide:
        tl = l[i+1].strip().split()
        k = int(tl[0])
        num =  int(tl[1])
        guide = False
        agmt = []
        
        
    else:
        agmt.append(int(l[i+1].strip()))
        c += 1 
        
        if c == k:
            c = 0
            guide = True
            print(dog_walker(agmt, num))
