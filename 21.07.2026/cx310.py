# Count the frequency of a particular character in a provided string. 
# Eg 'hello how are you' is the string, the frequency of h in this string is 2.


str=input("Enter a string : ")
rm=input("Enter the character to be removed : ")

result=""

for i in str:
    if(i!=rm):
        result=result+i

print("final ",result)        