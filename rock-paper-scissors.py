rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random 


# User input for rock, paper, scissors
player_choice = int(input("Input 0 for rock, 1 for paper and 2 for scissors:"))
#Computer generated random choice
computer_choice = random.randint(0,2)
choices = [rock, paper, scissors]

if player_choice == computer_choice:
  print("It's a tie.")
elif player_choice == 0 and computer_choice == 1:
  print("Player loses. Computer wins.")
elif player_choice == 0 and computer_choice == 2:
  print("Player wins. Computer loses.")
elif player_choice == 1 and computer_choice == 0:
  print("Player wins. Computer loses.")
elif player_choice == 1 and computer_choice == 2:
  print("Player loses. Computer wins.")
elif player_choice == 2 and computer_choice == 1:
  print("Player wins. Computer loses.")
elif player_choice == 2 and computer_choice == 0:
  print("Player loses. Computer wins.")
print(f"Player = {choices[player_choice]}")
print(f"Computer ={choices[computer_choice]}")