n=8

for i in range(n):
    for j in range(n):
        if(i+j)%2==0:
            print("x", end=" ")
        else:
            print("o", end=" ")
print()