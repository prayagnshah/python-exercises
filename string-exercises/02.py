s1 = "Ault"
s2 = "Kelly"

##finding the middle char of the string s1
l = len(s1)
i = int(l/2)
##finding all the chars before middle one 
x = s1[:i:]
##concatenating with string s2
x = x + s2 
##adding the remaining chars at the end of s1
x = x + s1[i:]
print(x)