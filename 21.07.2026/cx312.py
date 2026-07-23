# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

str =input("Enter a string : ")
rev=str[-1::-1]

if str==rev:
    print(str," : is a palindrome")
else:
    print(str," : is  not a palindrome")   
