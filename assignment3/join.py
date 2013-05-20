import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order identifier
    # value: record contents
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of records (order,lineitem)
    order = []    
    line_items = list([])
    for v in list_of_values:                
        if v[0] == 'order':
            order = v
        elif v[0] == 'line_item':
            line_items.append(v)  
    for li in line_items:
        rel = order + li
        mr.emit( rel)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
