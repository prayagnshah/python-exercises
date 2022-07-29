str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", "", False]

str_new = []  ##storing the new results into empty list

##iterating list and then using if condition to remove the empty strings
for i in str_list:
    if i:
        str_new.append(i)
print(str_new)
