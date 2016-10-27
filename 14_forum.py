import sys
def compute(res, a, p):
    map1=dict()
    map2=dict()
    List=[]
    for i in range(len(res)):
        if res[i]==0:
            map2[i]=i
        else:
            map2[i]=res[i]-1    
    for key in map2:
        key1=key
        while map2[key1]!=key1:
            key1=map2[key1]
        if key1 not in map1:
            map1[key1]=1
        else:
            map1[key1]+=1
    
            
    for k in sorted(map1.keys()):
        List.append(map1[k])
    n=len(List)
    worst=[0]*(n+1)
    worst[0]=0
    sum_tot=[0]*(n+1)
    sum_tot[0]=0
    for i in range(n):
        sum_tot[i+1]=sum_tot[i]+List[i]
    for i in range(n):
        j=i
        min_val=99999
        if sum_tot[i+1]<a:
            worst[i+1]=abs(a-sum_tot[i+1])
            continue
        while j>=0 and sum_tot[i+1]-sum_tot[j]-a<=worst[j]:
            min_val=min(min_val,max(worst[j],abs(sum_tot[i+1]-sum_tot[j]-a)))
            j-=1
        if j>=0:
            min_val=min(min_val,max(worst[j],abs(sum_tot[i+1]-sum_tot[j]-a)))   
        worst[i+1]=min_val              
    print(worst[n])
            
l = list(sys.stdin)
idx = 0
input = []
t = 0
res = []
while idx < len(l):
    a, p = l[idx].strip().split()
    idx += 1
    res=[]
    for i in range(int(p)):
        res.append(int(l[idx].strip()))
        idx+=1
    compute(res,int(a),int(p))
