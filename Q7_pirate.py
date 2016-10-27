import sys
from collections import defaultdict


def adj(b, pc):
    result = []
    m1 = len(b)
    n1 = len(b[0])
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=0 or j!=0:
                i1=pc[0]+i
                j1=pc[1]+j
                if i1<m1 and i1>=0 and j1<n1 and j1>=0:
                    result.append((i1,j1))
    
    return result

global group
group = 1
def visitSea(b, pc,visitedbool):
    global group
    visitedbool[pc[0]][pc[1]]=group
    List=[pc]
    while List!=[]:
        List1=[]
        for pc1 in List:
            for n in adj(b, pc1):
                if visitedbool[n[0]][n[1]] ==-1 and b[n[0]][n[1]] == '~':
                    global group
                    visitedbool[n[0]][n[1]]=group
                    List1.append(n)
        List=List1
                


def dfsSea(b,visitedbool):
    for i1 in range(len(b)):
        for i2 in range(len(b[0])):
            if b[i1][i2] == '~' and visitedbool[i1][i2]==-1:      
                visitSea(b, (i1,i2),visitedbool)
                global group
                group += 1


global groupLand
groupLand = 1
landDict = defaultdict(set)
def visit(b, pc, visitedbool):
    visitedbool[pc[0]][pc[1]]=groupLand
    List=[pc]
    while List!=[]:
        List1=[]
        for pc1 in List:
            for n in adj(b, pc1):
                if b[n[0]][n[1]] == '~':
                    global groupLand
                    landDict[groupLand].add(visitedbool[n[0]][n[1]])   
                elif visitedbool[n[0]][n[1]]==-1 and b[n[0]][n[1]] == 'O':
                    visitedbool[n[0]][n[1]]=groupLand
                    List1.append(n)
        List=List1
        
def dfs(b,visitedbool):
    for i1 in range(len(b)):
        for i2 in range(len(b[0])):
            if b[i1][i2] == 'O' and visitedbool[i1][i2]==-1:
                visit(b, (i1,i2),visitedbool)
                global groupLand
                groupLand += 1

            
    
    

            
    

sin = list(sys.stdin)
m, n, hp = sin[0].split()
m, n, hp = int(m), int(n), int(hp)

board = []
for i in range(1, 1+m):
    board.append(sin[i].strip())
    
visitedbool=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(-1)
    visitedbool.append(row)

#dfs(board)
dfsSea(board,visitedbool)
#print(visitedSea)

dfs(board,visitedbool)
#print(landDict)

def createDict(landDict):
    newDict=dict()
    for key in landDict:
        for i in landDict[key]:
            for j in landDict[key]:
                if i not in newDict:
                    newDict[i]=[]
                if j!=i:
                    newDict[i].append(j)
    return newDict
                    
bfsNb = createDict(landDict)
#print(bfsNb)


def bfs(nb, s, d):
    if s==d:
        return 0
    result = dict()
    depth = 0
    queue1 = [s]
    queue2=[d]
    global group
    visit1=[False]*group
    visit2=[False]*group
    while len(queue1)+len(queue2) > 0:
        explored1=[]
        explored2=[]
        for i in queue1:
            for j in nb[i]:
                if j==d:
                    return depth+1
                elif not visit1[j]:
                    if visit2[j]==True:
                        return 2*depth+1
                    else:
                        visit1[j]=True
                        explored1.append(j)

        for i in queue2:
            for j in nb[i]:
                if not visit2[j]:
                    if visit1[j]==True:
                        return 2*depth+2
                    else:
                        visit2[j]=True
                        explored2.append(j)    
        depth+=1
        
        
        queue1=explored1
        queue2=explored2
                
    return depth 
            
        


for i in range(1+m,len(sin)):
    s1, s2, d1, d2 = sin[i].strip().split()
    s1, s2, d1, d2 = int(s1)-1, int(s2)-1, int(d1)-1, int(d2)-1
    
    sg = visitedbool[s1][s2]
    dg = visitedbool[d1][d2]

    
    #print(sg,dg)


    print(bfs(bfsNb, sg, dg))
