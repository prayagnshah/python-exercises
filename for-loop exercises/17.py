n = 5
start = 2
sum_seq = 0

for i in range(0, n):
    print(start, end=" ")
    sum_seq += start
    start = start * 10 + 2
print(sum_seq)
