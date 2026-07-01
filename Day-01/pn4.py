str="hello world i am Gshyam"

t=(len(str))
for i in range(t):
    print(str[i],end="")

print()
for i in range(t-1,-1,-1):
    print(str[i],end="")

print()
for i in range(-1,-t-1,-1):
    print(str[i],end="")