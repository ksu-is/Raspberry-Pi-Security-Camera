username = 'rpi.alert.1@gmail.com'
password = 'AlphaZulu2923.'

userInput = input("What is your username? \n")

if userInput == username:
    userInput=input("Password?\n")
    if userInput == password:
        print("Welcome!")
    else:
        print("That is the wrong password.")
else:
    print("That is the wrong username.")
    
