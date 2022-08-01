import string

str1 = "/*Jon is @developer & musician!!"


# Replace punctuations with #
replace_char = "#"

# string.punctuation to get the list of all special symbols
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)

print(str1)
