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

person = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
rock_paper_scissors = [rock, paper, scissors]
print(rock_paper_scissors[person])

print("Computer chose:")

computer = random.randint(0,2)
print(rock_paper_scissors[computer])

if rock_paper_scissors[person] == rock_paper_scissors[computer]:
    print("It's a tie.")
elif rock_paper_scissors[person] == rock and rock_paper_scissors[computer] == scissors:
    print("You win.")
elif rock_paper_scissors[person] == paper and rock_paper_scissors[computer] == scissors:
    print("Computer win.")
elif rock_paper_scissors[person] == scissors and rock_paper_scissors[computer] == rock:
    print("Computer win.")
elif rock_paper_scissors[person] == paper and rock_paper_scissors[computer] == rock:
    print("You win.")
elif rock_paper_scissors[person] == rock and rock_paper_scissors[computer] == paper:
    print("Computer win.")
elif rock_paper_scissors[person] == scissors and rock_paper_scissors[computer] == paper:
    print("You win.")