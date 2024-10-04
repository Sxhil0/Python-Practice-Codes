n=int(input("Enter a Number:"))
for i in range(2,n):
    if (n%i==0):
        print(n,"is Not a Prime Number")
        break
else:
    print(n,"is a Prime Number")

## Prime_Numbers from a tuple
'''
tuple=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
for i in tuple:
    p=True
    for j in range(2,n):
        if (n%d==0):
            p=False
            break
    if p==True:
        print(i)
'''
