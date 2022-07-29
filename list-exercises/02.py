list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
##Adding the new data into the empty list
sum2 = []

for i, j in zip(list1, list2):   ## providing two different variables to i,j 
    sum1 = i + j                  ## adding to the list sum 
    sum2.append(sum1)     ##using append to add into the empty list
print(sum2)