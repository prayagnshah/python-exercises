str1 = "I am 25 years and 10 months old"

##iterating the string
for i in str1:
    if i.isdigit():  ##using .isdigit function to bring in only digits
        print(i, end="")
