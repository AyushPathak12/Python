import random as ayush
print("!-------------------------- Rock Scissor and Paper -----------------------------!")
print("Choose one of them \n 1 for Rock \n 2 for Scissor \n 3 for Paper")
print("Winning Rules of the Rock Scissor Paper game as follows: \n"
                                +"Rock vs Scissor->Rock wins \n"
                                +"Scissor vs Paper->scissor wins \n"
                                + "Paper vs Rock->Rock wins \n")
while True:
    choice = int(input("Your turn: "))

    if choice == 1:
      choice_name = 'Rock'
    elif choice == 2:
      choice_name = 'Scissor'
    elif choice == 3:
      choice_name = 'Paper'
    else:
      print("Wrong choice")
    print("user choice is: " + choice_name)
    print("Now its computer turn.......")
    comp_choice = ayush.randint(1, 3)
   
    if comp_choice == 1:
      comp_choice_name = 'Rock'
    elif comp_choice == 2:
      comp_choice_name = 'Scissor'
    else:
      comp_choice_name = 'Paper'
    print("Computer choice is: " + comp_choice_name)
  
    print(choice_name + " V/s " + comp_choice_name)  

  
    if (choice < comp_choice):
        print(choice_name + " wins", end = "")
        result = choice_name

    elif (choice > comp_choice):
        print(comp_choice_name + " Wins", end = "")
        result = comp_choice_name

    else:
      print("!---Tie---! ", end = "")

    if result == choice_name:
      print("<== User wins ==>")
    elif result == comp_choice_name:
      print("<== Computer wins ==>")
    else:
      print("<== No one wins ==>")
          
    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
      break 

print("\nThanks For Playing, Have A Nice Day!!!!\n")
