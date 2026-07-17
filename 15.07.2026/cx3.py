n=int(input("Enter the no :"))

sm=0
while(n>0):
    digit=n%10
    sm=sm+digit
    n=n//10

print(sm)
    

