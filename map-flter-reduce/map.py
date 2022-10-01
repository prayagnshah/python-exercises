numbers = ["12", "45", "46", "574"]

#using for loop
# for i in range(len(numbers)):
# numbers[i] = int(numbers[i])


##we want to use map funtion and then add the numbers to the 2nd position
# map function will make all the numbers in integer format

numbers = list(map(int,numbers))

numbers[2] = numbers[2] + 1  ##compulsory int can only go with int
print(numbers[2])


##using function and map at the same time

def square(num):
    return num*num

test_number = 5

result = print(square(test_number))


sq_num = list(map(square, numbers))

print(sq_num)

##using lambda and map at the same time

numbers = [1,2,34,5,53,42,23,11,2]
square_num = list(map(lambda s: s*s, numbers))
print(square_num)



##using map function and adding the numbers so concatenating int to list

def sum1(num1):
    num1 = num1 + 1
    return num1

num1 = [1,2,3,4,5,6,7]
value1 = map(sum1, num1)
print(list(value1))

