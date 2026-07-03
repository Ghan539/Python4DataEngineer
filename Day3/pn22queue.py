ls=[]
while(True):
    c= int(input('''
        1.push  elements
        2.pop first elements
        3.front element
        4.last element 
        5.display queue
        6.exit
    Enter choice :              
    '''))

    if (c==1):
       n=input("enter the value : ")
       ls.append(n)
       print(ls)

    elif (c==2):
        if(len(ls)==0):
            print("empty queue !")
        else:
            del ls[0] 
            print(ls)

    elif (c==3):
        if(len(ls)==0):
            print("empty queue !")
        else:
            print("front element : ",ls[0])

    elif (c==4):
        if(len(ls)==0):
            print("empty queue !")
        else:
            print("last element : ",ls[-1])



    elif(c==5) :
        print("display queue : " ,ls) 

    elif(c==6):
        break;
    else:
        print("invalid!!")

