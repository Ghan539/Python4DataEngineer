n=int(input("Enter a number :"))

series=0
fact=1
for i in range(1,n+1):
  print(i,end="+")  
  fact=fact*i
  series+=i/fact

print("=",series)
  