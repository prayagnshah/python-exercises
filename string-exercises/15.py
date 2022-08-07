import string

str1 = "/*Jon is @developer & musician"

##using maketrans of equal length in argument and then punctuation to remove it.
str2 = str1.maketrans("", "", string.punctuation)
print(str1.translate(str2))

print(str2)
