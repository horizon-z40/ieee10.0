import sys
from math import sqrt

def is_Prime(n):
    if n == 1 or n == 0:
        return False
    else:
        if n==3:
            return True
        if n%3==0:
            return False
        i=5
        while i*i<=n:
            if n % i == 0 or n%(i+2)==0:
                return False
            i=i+6
        return True
l = list(sys.stdin)
try:
    if long(l[0])==7:
        print 2,2,3
    else:
        for i in range(3):
            num = long(l[0])
            t=2*i+3
            num -= t
            x = t
            findanswer=False
            while num - 2*x >= 0:
                if is_Prime(x) and is_Prime(num - x): 
                    findanswer=True
                    print t, x, num - x
                    break
                else:
                    x += 2
            if findanswer:
                break
        if num - 2*x == 0:
            print("counterexample")
except:
    print("counterexample")
