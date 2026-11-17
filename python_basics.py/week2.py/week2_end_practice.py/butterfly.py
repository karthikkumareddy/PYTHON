n = 5

# Upper Half
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    for s in range(i,n-1):
        print(" ", end=" ")
    for s in range(i,n-1):
        print(" ",end = " ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Lower Half (Deeniki mundu unna extra spaces teesesamu)
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    for s in range(i):
        print(" ", end=" ")
    for s in range(i):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()
