list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

concatenate = []   ##empty list where data is stored. 

for i in list1:    ##using the nested loops 
    for j in list2:   
        sum1 = i+j     ##print individual items to each on in list2
        concatenate.append(sum1)
print(concatenate)
    