This is a repo for the Question 6 in the Assignment 4 for the CS 310 (Computational Geometry) class.

There are two versions of the algorithms: 1) numTri.py and 2) try.py.

1) This is the original version of the algorithm written in Python. We can run via

$ python3 numTri.py

While it only gives the length of the list right now, it should give the complete list of the diagonals for every triangulation
by adding 

print(numTri([0, 1, 2, ..., n]))

The largest n achieved by this was 17.

2) This is the modified version of the algorithm that uses Cython, attepting to make it run faster. 
This was created by compiling numTri.pyx by

$ python3 setup.py build_ext --inplace

and we can run it via

$ python3 try.py

The largest n achieved by this was 18.

(If python does not have cython, we can install it via

$ pip3 install Cython

)


The algorithm is built so that there is no overcount of a triangulation. We justify the correctness of the algorithm by 
explaining the outline of the algorithm as following:

1) We take an arbitrary vertex, namely Vertex 0, as a standard and consider the "yongest" diagonal that starts from 0. 
Here, we use "youngest" to indicate that the end point of the diagonal has the smallest index. Note that we can consider n-3 cases
where one of (0, i) (2<= i <= n-2) are the "youngest" and a case where there is no diagonal that starts from 0. 

2) 
i) We consider a case where there exists a diagonal from 0 and say (0, i) is the "youngest". (We iterate i from 2 to n-2.) 
Note that there are two polygons generated by the diagonal, namely L and R where the vertex n-1 is a vertex of R. 
(i.e. L is the left polygon and R is the right polygon when the vertex's index increase in ccw order)

ii) Notice that L = (0, 1, ...., i) and R = (0, i, ...., n-1). If L (R) has only three vertices, 
that polygon does not require any more diagonals. If R has more than three vertices, we recursively get all possible 
combinations of diagonals. For L with more than three vertices, since we have that (0, i) has to be the "youngest", 
there is no diagonal from 0. It follows from that (1, i) has to be a diagonal to have no overcounting. 
Therefore, we can recursively get all possible combinations of diagonals for L = (1, 2, ...., i). 

3) We consider a case where there does not exist a diagonal from 0. It follows that (1, n-1) is a diagonal, and it divides P into 
two polygons, namely A and B where A is a triangle (0, 1, n-1). We can recursively get all possible 
combinations of diagonals for B. 

As this algorithm considers the "youngest" diagonal for each call of numTri, it should be straight-forward that there is
no overcounting of a triangulation.

I'm really sorry but I didn't have enough time to think about the data structures.
