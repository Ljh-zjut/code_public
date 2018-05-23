def triangles():
    L=[1]
    n = 0
    while n < 10:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]
        n += 1
    return 'over'
for x in triangles():
    print(x)