from functools import reduce

##using the reduce function with lambda
##reduce(function, iterable)

list_1 = [1,2,4,3,42,4,2,42,6]

new_value = reduce(lambda x,y: x+y, list_1)

print(new_value)

##using the reduce function with normal def


##DOUBT why this funtion is asking for two positional arguments
def sq(a):
    return a > 5

new_val = reduce(sq,list_1)
print(new_val)