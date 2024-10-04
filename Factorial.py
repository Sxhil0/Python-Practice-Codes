def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a Number:"))
if isinstance(num,int) and num>0:
    print("Factorial=",factorial(num))
else:
    print("Cant Detect Factorial")
