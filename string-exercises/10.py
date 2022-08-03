str1 = "Apple"
##empty dictionary to store result
dict_1 = {}
##iterating characters of str1
for i in str1:
    # count = str1.count(i)  ##using .count option to count the charatcters
    # dict_1[i] = str1.count(i)
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1
print(dict_1)


# Method 2

# from collections import Counter   ##importing function counter to count the alphabets

# str1 = "Apple"

# res = Counter(str1)

# print(res)
