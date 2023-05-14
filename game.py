import random

def computer_choice():
	items = ["Rock", "Paper", "Scissors"]
	return random.choice(items)
    
#Game prompt

flag = True

while flag:
    get_computer_choise = computer_choice().lower()
    user_choice = input("Enter 'Rock','Paper' or 'Scissors' : ").lower()

    if user_choice == get_computer_choise:
        print("\nDraw ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif user_choice == "rock" and get_computer_choise == "scissors":
        print("\nYou Win ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif user_choice == "paper" and get_computer_choise == "rock":
        print("\nYou Win ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif user_choice == "scissors" and get_computer_choise == "paper":
        print("\nYou Win ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif get_computer_choise == "rock" and user_choice == "scissors":
        print("\nYou Lost ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif get_computer_choise == "paper" and user_choice == "rock":
        print("\nYou Lost ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif get_computer_choise == "scissors" and user_choice == "paper":
        print("\nYou Lost ! You entered : {} | Computer entered : {}".format(user_choice,get_computer_choise))
    elif user_choice.lower() == 'e':
        print("Thanks for playing !")
        flag = False
    else:
        print("Unknown user input")