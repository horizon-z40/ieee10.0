import sys
from math import factorial
l = list(sys.stdin)

def computesum(count,m):
    a=count[0]
    b=count[1]
    C=pow(10,9)+7
    sum=0
    if m>count[0]+2*count[1]:
        return 0
    for i in range(m/2+1):
        res=m-i*2
        if res>count[0] or i>count[1]:
            continue
        choose1=long(factorial(count[0])/factorial(res)/factorial(count[0]-res))
        choose2=long(factorial(count[1])/factorial(i)/factorial(count[1]-i))
        choose=((choose1%C)*(choose2%C))%C
        sum+=choose*((pow(25,i)%C)*(pow(24,res)%C)*(pow(2,count[0]-res)%C))%C
    return sum%C
        
        
        
   
        
        
        
        

def findpair(n,s):
    count=[0,0,0]
    if len(s)%2==1:
        count[2]=1
    length=len(s)
    C=pow(10,9)+7
    for i in range(length/2):
        if s[i]==s[length-1-i]:
            count[1]+=1
        else:
            count[0]+=1
    m=n-count[0]
    sum=0
    sum+=computesum(count,m)
    sum=sum%C
    if count[2]==1 and m>0:
        sum+=computesum(count,m-1)*25
    sum=sum%C
    return sum
    
    
    

t=int(l[0])
for i in range(t):
    t1=l[i+1].split()
    print(findpair(int(t1[0]),t1[1]))
    
