n = 5

for i in range(n):
    for j in range(n):
        if j == 0 or (i <= n//2 and i+1 == n-j) or (i > n//2 and i==j):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
