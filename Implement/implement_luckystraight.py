score = input()
length = 0
ls = []
for i in score:
    length += 1
    ls.append(int(i))
half = (length//2)
print(half)
a = sum(ls[0:half])

b = sum(ls[half:])
print(a, b)
if a == b:
    print("Lucky")
else:
    print("Ready")