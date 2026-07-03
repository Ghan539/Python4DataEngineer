ls=[]
while(True):
    c= int(input('''
        1.push elements
        2.pop elements
        3.peek elements 
        4.display stack 
        5. exit 
    Enter choice :              
    '''))

    if (c==1):
       n=input("enter the value : ")
       ls.append(n)
       print(ls)

    elif (c==2):
        if(len(ls)==0):
            print("empty stack !")
        else:
            p=ls.pop()
            print(p)
            print(ls)

    elif (c==3):
        if(len(ls)==0):
            print("empty stack !")
        else:
            print("top element : ",ls[-1])

    elif(c==4) :
        print("display stack : " ,ls) 

    elif(c==5):
        break;

