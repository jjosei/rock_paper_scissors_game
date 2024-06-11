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

# Write your code below this line 👇

import random

computer_input = random.randint(0, 2)

user_input = input("What do you choose? Rock, Paper or Scissors?\n").lower()

if user_input == "rock":
    print(rock)
elif user_input == "paper":
    print(paper)
elif user_input == "scissors":
    print(scissors)

if computer_input == 0:
    computer_choice = "rock"
elif computer_input == 1:
    computer_choice = "paper"
elif computer_input == 2:
    computer_choice = "scissors"

print("Computer chose:")

if computer_choice == "rock":
    print(rock)
elif computer_choice == "paper":
    print(paper)
elif computer_choice == "scissors":
    print(scissors)

if user_input == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_input == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_input == "paper" and computer_choice == "rock":
    print("You win!")
elif user_input == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_input == "scissors" and computer_choice == "rock":
    print("You lose!")
elif user_input == "paper" and computer_choice == "scissors":
    print("You lose!")
elif user_input == "paper" and computer_choice == "paper":
    print("Draw!")
elif user_input == "scissors" and computer_choice == "scissors":
    print("Draw!")
elif user_input == "rock" and computer_choice == "rock":
    print("Draw!")