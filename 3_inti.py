import sys

def findres(N,A):
    List=[]
    i=2;
    N0=N
    while i<=N and i*i<=N0:
        if N%i==0:
            List.append(i);
            while N%i==0:
                N=N/i
        i=i+1
    C=1000000007
    if N>1:
        List.append(N)
    sum=((A%C)*((A%C+1))/2)%C
    
    List_len=len(List)
    count=[long(0)]*1002000
    count[0]=-1
    t=1
    for i in range(List_len):
        z=t
        for j in range(z):
            count[t]=count[j]*List[i]*(-1)
            t=t+1
    for i in range(1,t): 
        num=A/abs(count[i])
        if num==0:
            continue
        sum=sum-(((num*(num+1))/2)*count[i])
        
        sum=sum%C
    return sum

l = list(sys.stdin)
agmt=[]
C=1000000007
for i in range(1,len(l)):
     t1 = l[i].strip().split()
     print((findres(long(t1[0]),long(t1[2]))-findres(long(t1[0]),long(t1[1])-1))%C)
