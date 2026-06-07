for num in range(100,1000):
    power=len(str(num))
    total=sum(int(d) ** power for d in str(num))
    if total==num:
        print(num)