def palindrome(value):
    return value==value[::-1]
value=input("Enter Something: ")
print(palindrome(value))
