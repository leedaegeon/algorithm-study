import sys
sys.setrecursionlimit(500000)



def append_star(LEN):
    if LEN == 1:
        return ['*']
    print(LEN)
    Stars = append_star(LEN // 3)
    L = []
    for S in Stars:
        print(S)
        L.append(S * 3)
    print("1 ",L)

    for S in Stars:
        print(S)

        L.append(S + ' ' * (LEN // 3) + S)
    print("2", L)

    for S in Stars:
        print(S)

        L.append(S * 3)
    print("3", L)
    return L


n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))

