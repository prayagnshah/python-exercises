rows = 5 

for i in range(0, rows + 1):   ##iterating first 5 numbers 
    for j in range(rows - i, 0, -1):   ##iterating the numbers from backwards using step -1
        print(j, end=" ")
    print()