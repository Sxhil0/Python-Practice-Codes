def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str
s = input("Enter your Name:")
print("The reversed string:",reverse(s))

#Another Way
'''
txt = "Hello World"[::-1]
print(txt)
'''