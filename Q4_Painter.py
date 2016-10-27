import sys

l = list(sys.stdin)
t = int(l[0])

guide = True
input = []
N = 1
for _ in range(t): 
    while N < len(l):
        line = l[N]
        N += 1
        if N % 2 != 0:
            input.append(line.strip())
            break

def paint( nums ):
    count = 0
    a = -1
    b = -1
    index = -1
    nums = nums.split()
    
    pos=[0]*21
    dic={}
    for i in range(21):
        dic[i]=[]
    for num in nums:
        index+=1
        dic[int(num)].append(index)
    
    index=-1
    
    for num in nums:
        index=index+1
        if int(num) == a or int(num) == b:
            if a==int(num):
                pos[a]+=1
            else:
                pos[b]+=1
            continue
        if a == -1:
            count += 1 
            a = int(num)
            pos[a]+=1
            continue
        if b == -1:
            count += 1
            b = int(num)
            pos[b]+=1
            continue
        else:
            count += 1
            if pos[a]==len(dic[a]):
                a = int(num)
                pos[a]+=1
                continue
            elif pos[b]==len(dic[b]):
                b = int(num)
                pos[b]+=1
                continue
            elif dic[a][pos[a]]<dic[b][pos[b]]:
                b = int(num)
                pos[b]+=1
            else:
                a = int(num)
                pos[a]+=1
       
        
        
    print(count)

for i in range(t):
    paint(input[i])

