str1 = "PyNaTive"  ##given string
str_new = ""   # adding the new data in the format of string. 

##iterating the string
for c in str1:
    if c.islower():  ##using the tool islower to print lowercase letters
        str_new = str_new + c

for c in str1:
    if c.isupper():  ##using the tool isupper to print uppercase letters
        str_new = str_new + c
print(str_new)
