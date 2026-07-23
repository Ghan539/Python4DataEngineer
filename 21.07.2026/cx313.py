# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

str =input("Enter a string : ")
ln=len(str)
mid=ln//2
flag=True
for i in range(mid):
    if str[i]!=str[-1-i]:
        flag=False
        break
    
if flag==True:
    print(" PALINDROME")    
    
else:
    print("not a palindrome")       
    
