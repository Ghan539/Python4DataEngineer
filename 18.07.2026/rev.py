n=int(input("Enter the no :"))


while(n>0):
    digit=n%10
    rev=digit
    n=n//10
    print(rev,end="")
