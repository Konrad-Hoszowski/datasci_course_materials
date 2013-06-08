import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

K=4 # rows in matrix A
L=4 # cols in matrix A and rows in matrix B
M=4 # cols in matrix B

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0] # matrix name
    r = record[1] # row index
    c = record[2] # col index
    v = record[3] # value of teh cell
    if matrix == 'a': # for matrix 'a' send cell value to all cols in target matrix for a given a.row
        for h in range(0,M+1):
          mr.emit_intermediate((r,h), record)
    if matrix == 'b': # for matrix 'b' send cell value to all rows in target matrix for a given b.col
        for j in range(0,K+1): 
          mr.emit_intermediate((j,c), record)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    k = key[0] # row in target matrix
    m = key[1] # col in target matrix
    ma = list([]) # cells from matrix a
    mb = dict([]) # cells from matrix b
    for i in list_of_values: #separate matrixes
        matrix = i[0]
        if matrix == 'a':
            ma.append(i)
        elif matrix == 'b':
            idx = i[1]
            mb[idx] = i
    #print key, '# ', list_of_values
    #print key, '# ', ma, ' * ',mb
    val = 0  # target value zero at beginning
    for acell in ma:
        col = acell[2]
        va = acell[3]
        vb = 0
        if col in mb:
            bcell = mb[col]
            vb = bcell[3]
        val+=va*vb
        
    mr.emit((k,m, val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
