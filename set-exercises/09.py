set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

##instead of giving a seperate variable we can use update to get the values
set2.intersection_update(set1)
print(set2)
