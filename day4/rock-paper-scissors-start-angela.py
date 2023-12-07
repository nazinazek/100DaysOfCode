import random

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

your_chose = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
rock_paper_scissors = [rock, paper, scissors]
if your_chose <= 2 and your_chose >= 0:
    print(rock_paper_scissors[your_chose])

    print("Computer chose:")

    computer_chose = random.randint(0,2)
    print(rock_paper_scissors[computer_chose])

    if your_chose == 0 and computer_chose == 2:
        print("You win.")
    elif your_chose == 2 and computer_chose == 0:
        print("You lose.")
    elif your_chose > computer_chose:
        print("You win.")
    elif your_chose < computer_chose:
        print("You lose.")
    elif your_chose == computer_chose:
        print("It's a tie.")
else: 
     print("You typed an invalid number. You loose")