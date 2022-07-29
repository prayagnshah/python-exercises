str1 = "Apple"
##empty dictionary to store result
dict_1 = {}
##iterating characters of str1
for i in str1:
    count = str1.count(i)  ##using .count option to count the charatcters
    dict_1[i] = count
print(dict_1)
