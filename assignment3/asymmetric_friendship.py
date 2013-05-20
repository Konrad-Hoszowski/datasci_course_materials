import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: friend A
    # value: friend B
    key = record[0]
    value = record[1]
    pair_key = hash(key) * hash(value)
    mr.emit_intermediate(pair_key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) < 2: 
        fa = list_of_values[0][0] 
        fb = list_of_values[0][1]      
        mr.emit((fa,fb))
        mr.emit((fb,fa))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
