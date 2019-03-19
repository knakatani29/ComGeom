# this is the function to count the number of triangulations
# for a convex polygon

# the input, n, is a list of vertices
def numTri(n):
    cdef int i, l, ly, lx, lz
    l = len(n)
    res = []
    # when there are only three vertices, it is already triangulated
    if l == 3:
        return []
    else:
        # Take the vertice on the head of the list, namely the vertice 0
        # as the standard
        # We first calculate the case where there exists a diagonal
        # that connects the vertice 0 and another.
        for i in range(2, l-1):
            y = [n[0]]
            for b in range(i, l):
                y += [n[b]]
            ly = len(y)
            q = []
            if i == 2:
                if ly == 3:
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
                lx = len(x)
                if lx == 3 and ly == 3:
                    q = q + [(n[1], n[i])]+ [(n[0], n[i])]
                    res += [q]
                elif lx == 3:
                    yy = numTri(y)
                    for h in yy:
                        q=[]
                        q = q + [(n[1], n[i])] +  [(n[0], n[i])] + h
                        res += [q]
                elif ly == 3:
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
        for c in range(1, l):
            z += [n[c]]
        lz = len(z)
        p = []
        if lz == 3:
            p = p + [(n[1], n[l-1])]
            res += [p]
        else:
            zz = numTri(z)
            for v in zz:
                p = []
                p = p + [(n[1], n[l-1])] + v
                res += [p]
    return res
