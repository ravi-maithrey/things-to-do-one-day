count = 0
for i in range(1, 99):
    count += 1
    for j in range(1, 101 - i):
        count += 1
        for k in range(1, 101 - (i + j)):
            count += 1
            if(i + j + k == 100 and 4*i + 2*j + (k/4) == 100):
                print(i, j, k, count)
#optimize this further
#use a count for each operation
print(count)