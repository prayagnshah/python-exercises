numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    
    # check if number is divisible by 5
    elif i % 5 == 0:
        print(i)
        