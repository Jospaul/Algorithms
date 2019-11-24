import re

ll = ['def30','abc40']
r = re.compile('\d+')
val = r.findall(','.join(l for l in ll))
sums=0
for v in val:
    sums+=int(v)

print(sums)

sums=0
for l in ll:
    x = r.findall(l)
    sums+=int(x[0])

print(sums)