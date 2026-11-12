# n= int(input())
# for i in range(1+n+1):
#     for j in range(i):
#         print(chr(65+j),end = " ")
#     print()
n = int(input())
nums = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+nums),end = " ")
        nums = nums + 1
    print()