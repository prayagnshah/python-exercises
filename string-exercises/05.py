str1 = "P@#yn26at^&i5ve"
##adding the filtered values in l,p and q
l=[]
p=[]
q=[]

## using the function isdigit, isalpha to print the filtered values from the string
for s in str1:
    if s.isdigit():
        l.append(s)
    elif s.isalpha():
        p.append(s)
    else:
        q.append(s)
        
##finding the lenght of the values to match with the output
c = len(l)
d = len(p)
e = len(q)
print("Digits: ", c)
print("Chars: ", d)
print("Symbol: ", e)