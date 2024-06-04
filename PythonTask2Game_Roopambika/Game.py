# Program to create a Rock-Paper-Scissors Game by Roopambika Mohanty
import random
def Game(user_choice, computer_choice):
  score = 0
  if user_choice == computer_choice:
      print(f"\nComputer chose {computer_choice}.Its a tie!\n")
  elif user_choice == 'Rock' and computer_choice == 'Paper' or user_choice == 'Paper' and computer_choice == 'Scissors' or user_choice == 'Scissors' and computer_choice == 'Rock':
      print(f"\nComputer chose {computer_choice}. You Lost!\n")
      score += -1
  elif user_choice == 'Rock' and computer_choice == 'Scissors' or user_choice == 'Paper' and computer_choice == 'Rock' or user_choice == 'Scissors' and computer_choice == 'Paper':
      print(f"\nComputer chose {computer_choice}.You Won!\n")
      score += 1
  else:
      print('\nInvalid Entry!(Enter Rock, Paper or Scissors). Try again\n')

  return score 

while True:
  user_choice = (input('Choose Rock, Paper or Scissors > '))
  options = ['Rock' , 'Paper' , 'Scissors']
  computer_choice = random.choice(options)
  score = Game(user_choice, computer_choice)
  print(f"\nYour score is {score} \n")

  play_again = input("\nDo you want to play again? (y/n): \n")
  if play_again=="n":
       print("Game ended")
       break
  elif  play_again=="y":
      continue
  else:
      raise ValueError("\nInvalid response!\n")