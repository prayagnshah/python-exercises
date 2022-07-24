tuple1 = (10, 20, 30, 40)

for i in range(len(tuple1)):    ##running tuple 1 for all the 4 numbers and satisfying all the conditions later on one by one
    if tuple1[i] == 10:
        print("print (a) will print", tuple1[i])
    elif tuple1[i] == 20:
        print("print (b) will print", tuple1[i])
    elif tuple1[i] == 30:
        print("print (c) will print", tuple1[i])
    else:
        print("print (d) will print", tuple1[i])