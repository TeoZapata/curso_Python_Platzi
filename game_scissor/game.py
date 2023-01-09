
import random

options = ("scissor","paper","rock")

def select_Option():
    computer_Option = random.choice(options)
    while True:
        user_Option = input("rock, Paper or scissor -> ")
        if user_Option.lower() in options:
            break
        else:
            print("Select a correct answer.\nTry again")  
    return computer_Option, user_Option



def check_game():
    comp , user = select_Option()
    if ((user.lower()=="scissor" and comp.lower()=="paper" ) 
        or (user.lower()=="paper" and comp.lower()=="rock" ) 
        or (user.lower()=="rock" and comp.lower()=="scissor" ) ):
        
        return True, user, comp
    elif user == comp:
        return None, user,comp
    else:
        return False, user, comp


def start_game():

    i = 1
    scoreComp = 0
    scoreUser = 0

    while i<6:

        print(f"\nRound {i}")
        print(f"Score user-> {scoreUser}")
        print(f"Score Computer-> {scoreComp}")

        status,user,comp=check_game()
        if status:
            scoreUser+=1
            print(f"win user \nUser->{user}\nComputer->{comp}")
            
        elif status == False:
            scoreComp+=1
            print(f"lose user \nUser->{user}\nComputer->{comp}")
            
        else:
            print(f"Tied \nUser->{user}\nComputer->{comp}")

        i+=1
        
    if scoreUser>scoreComp:
        print("\nWinning User")
        print(f"Score User -> {scoreUser}")
        print(f"Score Computer -> {scoreComp}")
    else:
        print("\nYou lose!")
        print(f"Score User -> {scoreUser}")
        print(f"Score Computer -> {scoreComp}")

start_game()