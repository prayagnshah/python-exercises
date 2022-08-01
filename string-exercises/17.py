str1 = "Emma25 is Data scientist50 and AI Expert"
s = str1.split()

##iterating the values and the checking the value with digits and alphabets

for i in s:
    if i.isalpha() == i.isdigit():
        print(i)
