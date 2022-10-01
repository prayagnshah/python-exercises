##Taking two different functions and then using map and lambda

def square(a):
    return a*a

def cube(b):
    return b*b*b

res = [square, cube]

for i in range(5):
    value = tuple(map(lambda x:x(i), res))
    print(value)


#**********

##using map function and adding the numbers so concatenating int to list

def sum1(num1):
    num1 = num1 + 1
    return num1

num1 = [1,2,3,4,5,6,7]
value1 = map(sum1, num1)
print(list(value1))
