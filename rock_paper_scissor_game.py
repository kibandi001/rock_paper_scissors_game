import random

print('''
Welcome to rock paper scissors. \n
The rules of the game are simple.\n
Rock vs Paper = Paper wins.\n
Rock vs scissors = Rock wins.\n
Paper vs Scissors = Scissors wins.\n
''')

chosen_name = None
comp_name = None
final_result = None

def main():
    global final_result
    print("You have three choices. \n1.Paper \n2.Rock \n3.Scissors")
    chosen_no = int(input("Now enter the number of your chosen: "))

    while chosen_no > 3 or chosen_no < 1:
        chosen_no = int(input("Entry invalid. Please chosse a valid input: "))

        if chosen_no <= 3 or chosen_no >= 1:
            break
    
    chosen(chosen_no)
    comp_chosen = random.randint(1, 3)
    com_turn(comp_chosen)
    print(f'{chosen_name} vs {comp_name}')
       
    #choosing a winner and a loser
    if ((chosen_name == 'paper' and comp_name == 'rock') or
        (chosen_name == 'rock' and comp_name == 'paper')):

        print("Paper wins")
        final_result = 'paper'


    elif ((chosen_name == 'paper' and comp_name == 'scissors') or
          (chosen_name == 'scissors' and comp_name == 'paper')):

        print('Scissors wins')
        final_result = 'scissors'

    elif ((chosen_name == 'rock' and comp_name == 'scissors') or
          (chosen_name == 'scissors' and comp_name == 'rock')):

        print('Rock wins')
        final_result = 'rock'

    elif (chosen_name == comp_name):
        print('Its a tie!!')
    
    #print who won
    if final_result == chosen_name:
        print('<// You won!!!!!! //>')
    elif final_result == comp_name:
        print('<** The computer won **>')
    
    # prompt for playing again
    print("Want to play again? (Y/N)")
    answer = input()
    answers = ['y', 'Y', 'n', 'N']
    if answer in answers:
        if answer == 'n' or answer == 'N':
            print('GoodBye')
        else:
            main()
    else:
        while answer not in answers:
            print('Invalid Entry. Please try again: ')
            ans = input()
            if ans in answers:
                if ans == 'n' or ans == 'N':
                    print('GoodBye')
                    break
                else:
                    main()
                    
        
        
    

def chosen(chosen_no):
    global chosen_name
    
    if chosen_no == 1:
        chosen_name = 'paper'
        
    elif chosen_no == 2:
        chosen_name = 'rock'

    elif chosen_no == 3:
        chosen_name = 'scissors'

    else:
        print("Dont know what you are talking about!")
        print('Are you sure you want to play? (Y/N)')
        ans = input()
        if ans == 'n' or ans == 'N':
            print('GoodBye')
        else:
            main()

def com_turn(comp_chosen):
    global comp_name

    if comp_chosen == 1:
        comp_name = 'paper'

    elif comp_chosen == 2:
        comp_name = 'rock'

    else:
        comp_name= 'scissors'

   



if __name__ == '__main__':
    main()
        
