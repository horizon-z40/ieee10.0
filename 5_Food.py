import sys
from math import radians, asin, sin, cos, sqrt
from datetime import datetime
def compute(o, radius, d):
    r = 6378.137 
    lat1, long1 = o
    lat2, long2 = d
    long1, lat1, long2, lat2 = map(radians, [long1, lat1, long2, lat2])
    dis=sqrt( sin ( ( lat1-lat2 ) / 2.0 ) ** 2 + cos( lat1 )* cos(lat2) * sin( (long1-long2 )/ 2.0 )**2 )
    return sin(radius/2.0/r)>=dis

l = list(sys.stdin)
person = l[0].split(",")
person = [float(i) for i in person]
radius = float(l[1])
index = 3
input1 = []
dic = {}
dic1={}
while index < len(l):
    line = l[index].split(",")
    d = (float(line[1]), float(line[2]))
    number = line[3].strip()
    rizi, shijian = line[0].split()
    yue, ri, nian = rizi.split("/")
    shi, fen = shijian.split(":")
    time = nian + yue + ri + shi + fen
    if number in dic:
        if time > dic[number]:
            dic[number] = time
            dic1[number]=d
    else:
        dic[number] = time
        dic1[number]=d
    index+=1

for number in dic:
    if compute(person, radius, dic1[number]):
        input1.append(number)

input1 = sorted(input1)
print(",".join(input1))
