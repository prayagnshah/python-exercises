set1 = {10, 20, 30}
set2 = {20, 40, 50}

# ##using difference function to find the set1 which don't exist in set2
# print("set1", set1.difference(set2))

for i in list(set1):
    if i in set2:
        set1.remove(i)
print(set1)
