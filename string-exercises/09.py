str1 = "PYnative29@#8496"
total = 0
cnt = 0
##using the function isdigit to find the digits 
for i in str1:
    if i.isdigit():
        total = total + int(i)
        cnt = cnt + 1
##using to find the average of the numbers       
avg = total / cnt
print(total, avg)