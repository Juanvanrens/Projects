#Rock Paper Scissors
import random
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper =  '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
Scissors =  '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Rock[0] beats scissors[2]
#Paper[1] beats rock[0]
#scissors[2] beat paper[1]

Computer_Selection = random.randint(0, 2)
print("Welcome to the Rock Paper Scissors game!\n")
User_Selection = int(input("Choose [0] for Rock , [1] for Paper , [2] for Scissors \n"))


if User_Selection <0 or User_Selection > 2:
    print("Invalid Selection")
    exit(0)

print(f"You choose {User_Selection}")
print(f"Computer Chooses {Computer_Selection}")

if User_Selection == Computer_Selection == 0:
    print(f"\nYou have chosen rock:\n {Rock}\n")
    print(f"The Computer has chosen rock:\n {Rock}\n")
    print(f"Draw")

elif User_Selection == Computer_Selection == 1:
    print(f"\nYou have chosen paper:\n {Paper}\n")
    print(f"The Computer has chosen paper:\n {Paper}\n")
    print(f"Draw")

elif User_Selection == Computer_Selection == 2:
    print(f"\nYou have chosen scissors:\n {Scissors}\n")
    print(f"The Computer has chosen scissors:\n {Scissors}\n")
    print(f"Draw")


elif User_Selection == 0 and Computer_Selection == 2:

    print(f"\nYou have chosen rock:\n {Rock}\n")
    print(f"The Computer has chosen scissors:\n {Scissors}\n")
    print(f"You Win")

elif User_Selection == 2 and Computer_Selection == 0:
    print(f"\nYou have chosen scissors:\n {Scissors}\n")
    print(f"The Computer has chosen rock:\n {Rock}\n")
    print(f"You Loose")

elif User_Selection == 1 and Computer_Selection == 0:
    print(f"\nYou have chosen paper:\n {Paper}\n")
    print(f"The Computer has chosen rock:\n {Rock}\n")
    print(f"You Win")

elif User_Selection == 0 and Computer_Selection == 1:
    print(f"\nYou have chosen rock:\n {Rock}\n")
    print(f"The Computer has chosen paper:\n {Paper}\n")
    print(f"You Loose")

elif User_Selection == 2 and Computer_Selection == 1:
    print(f"\nYou have chosen scissors:\n {Scissors}\n")
    print(f"The Computer has chosen paper:\n {Paper}\n")
    print(f"You Win")

elif User_Selection == 1 and Computer_Selection == 2:
    print(f"\nYou have chosen paper:\n {Paper}\n")
    print(f"The Computer has chosen scissors:\n {Scissors}\n")
    print(f"You Loose")








