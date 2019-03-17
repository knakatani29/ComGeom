# this is the function to count the number of triangulations
# for a convex polygon
def numTri(n):
    res == []
    if len(n) == 3:
        return 
    else:
        for i in range(3, len(n)):
            x = []
            y = []
            for a in range(i):
                x += [n[a]]
            for b in range(i-1, len(n)):
                y += [n[b]]
            res += [[numTri(x), (n[0], n[i]), numTri(y)]]
        z = []
        for c in range(1, len(n)):
            z += [n[c]]
        res += [[numTri(z), (n[1], n[len(n)-1])]]
    print(len(res))
    return res
        
