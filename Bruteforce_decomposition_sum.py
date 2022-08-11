# -*- coding: utf-8 -*-

n = input()
intn = int(n)
a = []
mresult = 1000000
temp = 0
for j in range(0,intn):
    l = len(str(j))
    temp = j
    for i in range(0,len(str(j))):

        a.append(j//(10**(l-1)))
        j =j % (10**(l-1))
        j = int(j)
        l -= 1
    if temp + sum(a) == intn and mresult > intn:
        mresult = temp

    a.clear()
if mresult != 1000000:
    print(mresult)
else:
    print(0)