##trying to use the filter function by creating a function

list_1 = [1,2,4,3,42,4,2,42,6]

def less_than(a):
    return a > 5

val = list(filter(less_than, list_1))

print(val)

#**************using the same above example without using filter**************

new_res = []
for i in range(0, len(list_1)):
    if list_1[i] > 5:
        new_res.append(list_1[i])
print(new_res)



##trying to use the filter using the lambda function

list_2 = [0,1,2,34,34,532,12,4,6,17]

value = filter(lambda x:x%2==0, list_2)

print(list(value))


##examples using the filter() function

numbers = [-2, -1, 0, 1, 2]

num = filter(lambda n: n>0, numbers)
print(list(num))