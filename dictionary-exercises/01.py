keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]

length = len(keys)  ##finding the length of the var keys
size = len(values)

for i in range(length):  # using for loop to reiterate the value of keys
    print(keys[i], ":", values[i], end=" ")
