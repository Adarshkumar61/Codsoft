import random

def game():
    user_choice = input("Enter your choice: ")
    choices = ["rock", "paper", "scissor"]
    com_choice = random.choice(choices)
    
    if user_choice == com_choice:
        print("computer choosed: ", com_choice)
        print("Match tie")
    elif(user_choice == "rock" and com_choice == "scissor") or \
        (user_choice == "paper" and com_choice == "rock") or \
        (user_choice == "scissor" and com_choice == "paper"):
        print("computer choosed: ", com_choice)
        print("You win... Hurrrahh.....")
        
    else:
        print("computer choosed: ", com_choice)
        print("Computer win")
    ask = input("want to play again ?").lower()
    if ask == "yes":
        game()
    else:
        print("thanku for playing")     
game()
    