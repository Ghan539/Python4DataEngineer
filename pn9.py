ls=ls=[12,23,34,"hello",(23,54,78),[12,23,54,"hello"]]
ln=len(ls)
for i in range(-1,-ln-1,-1):
    print(ls[i],end=" ")

print("\nanother")

for i in range(ln-1,-1,-1):
     print(ls[i],end=" ")