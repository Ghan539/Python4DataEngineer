dict={
    'name':'ghanshyam',
    'age':24,
    'course':'Btech',
    'duration':'4 year'
}

g=dict.get('name')
g1=dict['name']

print(g)
print(g1)

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)    

for i,j in dict.items():
    print(i,j)

del dict['age']
n=dict.pop('course')

for i,j in dict.items():
    print(i,j)