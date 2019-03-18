# this is the function to count the number of triangulations
# for a convex polygon

def numTri(n):
    res = []
    if len(n) == 3:
        return []
    else:
        for i in range(2, len(n)-1):
            x = []
            y = [n[0]]
            for a in range(1, i+1):
                x += [n[a]]
            for b in range(i, len(n)):
                y += [n[b]]
            q = []
            yy = numTri(y)
            if len(x)==2:
                if yy == []:
                    q = q  + [(n[0], n[i])]
                    res += [q]
                else:
                    for h in yy:
                        q=[]
                        q = q + [(n[0], n[i])] + h
                        res += [q]
            else:   
                q = []
                xx = numTri(x)
                yy = numTri(y)
                if xx == [] and yy == []:
                    q = q + [(n[1], n[i])]+ [(n[0], n[i])]
                    res += [q]
                elif xx == []:
                    for h in yy:
                        q=[]
                        q = q + [(n[1], n[i])] +  [(n[0], n[i])] + h
                        res += [q]
                elif yy == []:
                    for k in xx:
                        q=[]
                        q = q + k + [(n[1], n[i])] +  [(n[0], n[i])]
                        res += [q]
                else:
                    for k in xx:
                        for h in yy:
                            q=[]
                            q = q + k + [(n[1], n[i])] + [(n[0], n[i])] + h
                            res += [q]
        z = []
        for c in range(1, len(n)):
            z += [n[c]]
        p = []
        zz = numTri(z)
        if zz == []:
            p = p + [(n[1], n[len(n)-1])]
            res += [p]
        else:
            for v in range(len(zz)):
                p=[]
                p = p + [(n[1], n[len(n)-1])] + zz[v]
                res += [p]
    return res

print(len(numTri([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17])))
