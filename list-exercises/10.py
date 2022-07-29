list1 = [5, 20, 15, 20, 25, 50, 20]

list2 = []   ##empty where we will store new numbers

for i in list1:    ##running loop for all the numbers
    if i != 20:    ##condition
        list2.append(i)   ##adding the new data to the empty list
print(list2)       