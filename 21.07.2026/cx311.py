# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.


str=input("Enter a string : ")
rm=input("Enter the character to be removed : ")

result=str.replace(rm,'')

print("final ",result) 
       