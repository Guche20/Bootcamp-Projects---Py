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
choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
Computer_chose = random.randint(0,2)
if choice < 0 or choice >= 2:
  print("You entered an invalid number. You lose!")
elif choice == 0:
  print(rock)
  print("Computer chose")
  if Computer_chose == 0:
    print(f"{rock}\nDraw")
  elif Computer_chose == 1:
    print(f"{paper}\nYou lose")
  else:
    print(f"{scissors}\nYou win")
elif choice == 1:
  print(paper)
  print(f"Computer chose")
  if Computer_chose == 0:
    print(f"{rock}\nYou win")
  elif Computer_chose == 1:
    print(f"{paper}\nDraw")
  else:
    print(f"{scissors}\nYou lose")
else:
  print(scissors)
  print(f"Computer chose")
  if Computer_chose == 0:
    print(f"{rock}\nYou lose")
  elif Computer_chose == 1:
    print(f"{paper}\nYou win")
  else:
    print(f"{scissors}\nDraw")