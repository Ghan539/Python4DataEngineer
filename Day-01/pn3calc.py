while(True):
    num1=eval(input("Enter num1 :"))
    num2=eval(input("Enter num2 :"))

    opr=input("enter the operator :")

    if(opr=="+"):
        print(num1+num2)
    elif(opr=="-"):
        print(num1-num2)
    elif(opr=="*"):
        print(num1*num2)
    elif(opr=="/"):
        print(num1/num2)            
    elif(opr=="%"):
        print(num1%num2)
    else:
        print("invalid operator")  


    choice=input("want to continue y / n  : ")

    if(choice.lower()=="n"):
       print("thank you ")
       break;