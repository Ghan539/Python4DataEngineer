import random

jackpot=random.randint(1,100)

guess=int(input("guess number(1,100) : "))
counter=1
while guess!=jackpot:
    if guess<jackpot:
        print("wrong!,guess higher ")
    else:
        print("wrong!, guess lower")   
    guess=int(input("guess number(1,100) : "))
    counter+=1

else:
    print("correct guess,in",counter,"attempts")
    