import time
import sys
start = time.time()
instr = sys.stdin.readline().strip()
char_ls = []
sum_val = 0

for i in instr:
    #if "A" <= i <= "Z":
    #char.isalpha()가 훨씬 빠름
    if i.isalpha():
        char_ls.append(i)
    else:
        sum_val += int(i)

char_ls.sort()
print("".join(char_ls), end = "")
print(sum_val)
print(time.time() - start)