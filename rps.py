import random

def choose_random():
    return random.randint(0,2)
    

def check_win(input_1, input_2):
    win_options = ["Tie!", "Win!", "Lose!"]
    diff = input_1 - input_2
    return win_options[diff %3]
'''
    if diff == 0:
        return "Tie!"
    elif diff % 3 == 2:
        return "Loss!"
    elif diff % 3 == 1:
        return "Win!"
    else:
        return "Something went wrong"
    '''
    
def get_user_input():
    vaild_input = False 
    while not vaild_input: 
        user_input = input("Rock(0), Paper(1), Or Scissors(2): (q) to quit: ")
        if user_input == "q":
            return user_input
        elif user_input == "0" or user_input == "1" or user_input == "2":
            vaild_input = True 
            return int(user_input)
        else:
            print("Invaild Input! Read the directions and try")





game_going = True
options = ["Rock", "Paper", "Scissors"]
while game_going:
    user_input = get_user_input()
    if user_input == "q":
        break
    computer_input = choose_random()
    print(f"You Choose: {options[user_input]}. Computer choose: {options[computer_input]} ")
    print(check_win(user_input, computer_input))

        
''' def check_win(input_1, input_2):
    if input_1 == input_2:
        return "Tie!"
    elif input_1 == 0 and input_2 == 1:
        return "Lose!"
    elif input_1 == 0 and input_2 == 2:
        return "Win!"
    elif input_1 == 1 and input_2 == 0:
        return "Win!"
    elif input_1 == 1 and input_2 == 2:
        return "Lose!"
    elif input_1 == 2 and input_2 == 0:
        return "Lose!"
    elif input_1 == 1 and input_2 == 1:
        return "Win!"
    else:
        return "Something went wrong..."
'''
