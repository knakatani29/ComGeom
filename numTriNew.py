# this is the function to count the number of triangulations
# for a convex polygon

# the input, n, is a list of vertices

def numTri(n):
    res = []
    # when there are only three vertices, it is already triangulated
    if len(n) == 3:
        return []
    else:
        # Take the vertice on the head of the list, namely the vertice 0
        # as the standard
        # We first calculate the case where there exists a diagonal
        # that connects the vertice 0 and another.
        for i in range(2, len(n)-1):
            y = [n[0]]
            for b in range(i, len(n)):
                y += [n[b]]
            q = []
            if i == 2:
                if len(y) == 3:
                    q = q  + [(n[0], n[i])]
                    res += [q]
                else:
                    yy = numTri(y)
                    for h in yy:
                        q = []
                        q = q + [(n[0], n[i])] + h
                        res += [q]
            else:
                x = []
                for a in range(1, i+1):
                    x += [n[a]]
                if len(x) == 3 and len(y) == 3:
                    q = q + [(n[1], n[i])]+ [(n[0], n[i])]
                    res += [q]
                elif len(x) == 3:
                    yy = numTri(y)
                    for h in yy:
                        q=[]
                        q = q + [(n[1], n[i])] +  [(n[0], n[i])] + h
                        res += [q]
                elif len(y) == 3:
                    xx = numTri(x)
                    for k in xx:
                        q=[]
                        q = q + k + [(n[1], n[i])] +  [(n[0], n[i])]
                        res += [q]
                else:
                    xx = numTri(x)
                    yy = numTri(y)
                    for k in xx:
                        for h in yy:
                            q=[]
                            q = q + k + [(n[1], n[i])] + [(n[0], n[i])] + h
                            res += [q]
        # When there does not exist a diagonal at the vertex 0
        z = []
        for c in range(1, len(n)):
            z += [n[c]]
        p = []
        if len(z) == 3:
            p = p + [(n[1], n[len(n)-1])]
            res += [p]
        else:
            zz = numTri(z)
            for v in zz:
                p = []
                p = p + [(n[1], n[len(n)-1])] + v
                res += [p]
    return res

print(len(numTri([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])))
