str1 = "P@#yn26at^&i5ve"
##adding the filtered values in l,p and q
digits_list = []
alphabets_list = []
symbol_list = []

## using the function isdigit, isalpha to print the filtered values from the string
for s in str1:
    if s.isdigit():
        digits_list.append(s)
    elif s.isalpha():
        alphabets_list.append(s)
    else:
        symbol_list.append(s)

##finding the lenght of the values to match with the output
digit_count = len(digits_list)
alphabet_count = len(alphabets_list)
symbol_count = len(symbol_list)
print("Digits: ", digit_count)
print("Chars: ", alphabet_count)
print("Symbol: ", symbol_count)
