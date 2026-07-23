# Extract username from a given email. 
# Eg if the email is nitish24singh@gmail.com 
# then the username should be nitish24singh


email=input("Enter a email : ")
pos=email.find("@")
usr=email[0:pos]
print(usr)