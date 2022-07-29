num1, num2 = 0, 1
#itearting first 10 numbers
for i in range(10):
    print(num1,",",  end ="")
    #adding last two numbers to get next two numbers
    res = num1 + num2
    #adding values in num2
    num1 = num2
    num2 = res