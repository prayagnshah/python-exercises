n = 6  # writing this number to select rows

## iterating the numbers from 1 to 5 and in ascending order using nested loops
for i in range(1, n):
    for j in range(i):  ##loop inside loop to print 1 to 5
        print("*", end=" ")
    print(" ")

##iterating numbers in descending order
for k in range(n - 1, 0, -1):
    for l in range(0, k - 1):
        print("*", end=" ")
    print(" ")
