import random

target=random.randint(1,100)
while True:
    userChoice =input("gess the target or Quit(Q) :")
    if(userChoice=="Q"):
        break
    userChoice=int(userChoice)
    if(userChoice==target):
        print("Success:Correct Guess")
        break
    elif(userChoice < target):
        print("your GUESS is too SMALL")
    else:
        print("your GUESS is too BIG")

print("-------GAME OVER---------")        
