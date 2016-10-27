import sys
import math

def findnum(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n%2==0:
        return findnum(n/2)*2-1
    else:
        t=findnum(1+n/2)
        if t==1:
            return n
        else:
            return (t-1)*2-1

sin = list(sys.stdin)[1:]

for n in sin:
    num = long(n)
    print(findnum(num))
