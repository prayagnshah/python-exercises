str1 = "I am 25 years and 10 months old"
numbers = ""

##iterating the string
for i in str1:
    if i.isdigit():  ##using .isdigit function to bring in only digits
        numbers += i  ##this is used in order to save in string
print(numbers)


## trying to use for loop shorthand

# numbers_1 = [i for i in str1 if i.isdigit()]


# print("".join(numbers_1))
