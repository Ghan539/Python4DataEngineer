course={
    'php':{'duration':'3 months','fees':'15000'},
    'java':{'duration':'2 months','fees':'35000'},
    'python':{'duration':'1 months','fees':'50000'},
    
}

course['java']['fees']=66000

for i,j in course.items():
    print(i,j)

for i in course.values():
    print(i)

for i,j in course.items():
    print(i,j['duration'],j['fees'])    