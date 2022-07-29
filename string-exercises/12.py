str1 = "Emma is a data scientist who knows Python. Emma works at google."
##iterating the whole string
for i in str1:
    find = str1.rfind("Emma")  ##finding the last occurence witht help of rfind function
print(find)
