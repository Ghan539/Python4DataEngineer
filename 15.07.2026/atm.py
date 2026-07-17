pin=int(input("Enter your ATM pin :"))
bal=5000
atmpin=2620
while(True):
    if(atmpin==pin):
     print("""welcome to hdfc....
      1.check balance 
      2.withdraw
      3.deposit
      4.Exit      
         """)
     choice=int(input("Enter choice :"))
     if(choice==1):
        print("your balance :",bal)
     elif(choice==2):
        withdraw=int(input("enter amount to withdraw :"))
        if(withdraw<=bal):
            bal=bal-withdraw
            print("your current balance :",bal)
        else:
            print("insufficient balance ")  
     elif(choice==3):
        deposit=int(input("enter amount to deposit :"))
        bal=bal+deposit
        print("your current balance :",bal)
     elif(choice==4):
        print("Thank u banking with us..") 
        break;
        
     else:
        print("invalid choice")
        
    else:
       print("wrong pin")
       reset=int(input("reset your pin : "))
       atmpin=reset
       pin = int(input("Enter your ATM PIN: "))
    
    