for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                print(num)
                break
            else:
                print("None")
