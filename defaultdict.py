from collections import defaultdict
d = defaultdict(list)

n,m = map(int, input().split())

for i in range(1, n+1):
    d[input()].append(i)

mlist = [input() for _ in range(m)]

for i in mlist:
    if i in d.keys():
        print(" ".join(map(str, d[i])))
    else:
        print(-1)
