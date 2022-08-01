str1 = "James"
new_str = ""
##iterating even number of characters
for i in range(0, len(str1), 2):
    new_str += str1[i]
print(new_str)
