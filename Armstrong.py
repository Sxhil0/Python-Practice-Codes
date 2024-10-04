def armstrong(num):
    digits=str(num)
    num_digits=len(digits)
    armstrong_sum=sum(int(digit)**num_digits for digit in digits)
    return armstrong_sum==num

num=int(input("Enter a number: "))
if armstrong(num):
    print(num," is an Armstrong number.")
else:
    print(num," is not an Armstrong number.")
