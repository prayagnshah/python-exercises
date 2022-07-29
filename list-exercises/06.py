list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
##Adding the new data into the empty list
list2 = []
for i in list1:  ##run the list1 iteration
    if i != "":   ##condition 
        list2.append(i)   ##adding into the empty variable list2
print(list2)
    