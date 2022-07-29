##defining a function for string balance
def string_test(s1,s2):
    ##providing boolean expression
    flag = True
    for i in s1:
        if i in s2:   ##condiiton used to check that if first string is present in second or not
            continue
        else:
            flag = False
    return flag
    
s1 = "Yn"
s2 = "PYnative"
print("Strings are balanced: ", string_test(s1,s2))

s1 = "Ynf"
s2 = "PYnative"
print("Strings are balanced: ", string_test(s1,s2))