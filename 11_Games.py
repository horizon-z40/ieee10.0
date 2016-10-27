import sys

lines = list(sys.stdin)
t = int(lines[0])
idx = 1
for _ in range(t):
    numGames = int(lines[idx])
    idx += 1 
    res = 0
    for i in range(numGames * 2):
        if i % 2 :
            p = lines[idx].split()
            for x in p:
                res += int(x) / 2
        idx += 1
    print( "Alice" ) if res % 2 else ("Bob")
