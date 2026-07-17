email=input("Enter your email : ")
password=input("Enter password : ")

if(email=="ghanshyam.seervi1296@gmail.com" and password=="8013402620"):
    print("welcome")
elif (email=="ghanshyam.seervi1296@gmail.com" and password!="8013402620"):  
    print("wrong password")
    password=input("Enter password again :")
    if(password=="801340"):
        print("welcome finally ")
    else:
        print("try again !!!") 

elif (email!="ghanshyam.seervi1296@gmail.com" and password=="8013402620"):  
    print("wrong email ")
    email=input("Enter email again :")
    if(email=="ghanshyam.seervi1296@gmail.com"):
        print("welcome finally ")
    else:
        print("try again !!!") 
else:
    print("recheck email or password")       