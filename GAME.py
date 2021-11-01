import random as ayush
print("!-------------------------- Rock Paper and Scissor -----------------------------!")
print("Choose one of them \n r for Rock \n p for Paper \n s for Scissor")
print("Winning Rules of the Rock Paper Scissor game as follows: \n"
                                +"Rock vs Paper->Paper wins \n"
                                + "Rock vs Scissor->Rock wins \n"
                                +"Paper vs Scissor->Scissor wins \n")
while True:
    choice = int(input("Your turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
    if choice == 1:
      choice_name = 'Rock'
    elif choice == 2:
      choice_name = 'Paper'
    else:
      choice_name = 'Scissor'
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")
    comp_choice = ayush.randint(1, 3)
    while comp_choice == choice:
      comp_choice = ayush.randint(1, 3)
    if comp_choice == 1:
      comp_choice_name = 'Rock'
    elif comp_choice == 2:
      comp_choice_name = 'Paper'
    else:
      comp_choice_name = 'Scissor'
    print("Computer choice is: " + comp_choice_name)
  
    print(choice_name + " V/s " + comp_choice_name)                        
    if ((choice == 1 and comp_choice == 2) or
        choice == 2 and comp_choice == 1):
      print("Paper wins => ", end = "")
      result="Paper"

    elif ((choice == 3 and comp_choice == 1) or
          choice == 1 and comp_choice == 3):
      print("Rock wins => ", end = "")
      result="Rock"

    else:
      print("Scissor wins => ", end = "")
      result="Scissor"
    if result == choice_name:
      print("<== User wins ==>")
    else:
      print("<== Computer wins ==>")
          
    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
      break 

print("\nThanks For Playing, Have A Nice Day!!!!")
