def palindrome(value):
    value_str=str(value)
    start=0
    end=len(value_str)-1
    while start<end:
        if value_str[start]!=value_str[end]:
            return False  # Not a palindrome
        start+=1
        end-=1
    return True  # Is a palindrome
sn=input("Enter a string or number: ")
if palindrome(sn):
    print(sn,"is a palindrome")
else:
    print(sn,"is not a palindrome")
