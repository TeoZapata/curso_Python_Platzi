
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


print(check_game())