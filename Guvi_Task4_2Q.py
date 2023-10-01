rows = 6 # declaring the
startnum = 1
for i in range(1, rows + 1):
    for j in range(rows - i):  # for adding the space between the numbers
        print(" ", end=" ")
    for k in range(1, i + 1):  # to print numbers in order
        print(startnum, end=" ")
        startnum += 1
    print()
