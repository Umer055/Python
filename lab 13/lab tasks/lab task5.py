for i in range(1, 5):
    for j in range(1,5-i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(2 ** (k-1), end=" ")
    for l in range (i,1,-1):
        print(2**(l-2),end=" ")
    print()
