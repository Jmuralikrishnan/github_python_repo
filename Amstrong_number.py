num=int(input("enter a number :  "))

num_str=str(num)
num_digits=len(num_str)

digit_sum=sum(int(digit)**num_digits for digit in num_str)

if digit_sum == num:
    print(f"{num} is an amstrong number")
else:
    print(f"{num} is not an amstrong number")