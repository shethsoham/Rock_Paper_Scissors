import random
rock = '''
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

your_choice = int(input("Enter the number between 0,1 or 2"))


if your_choice == 0:
  print(rock)
elif(your_choice == 1):
  print(paper)
elif(your_choice == 2):
  print(scissors)


computer_choice = [rock, paper, scissors]
choice_len = len(computer_choice)
computer_select = random.randint(0, choice_len - 1)
print("Computer Choose ",computer_select)
print(computer_choice[computer_select])



if your_choice == computer_select:
  print("Draw")
elif (your_choice != computer_select ):
  if(your_choice == 0 and computer_select == 1):
    print("You Loose")
  elif(your_choice == 0 and computer_select == 2):
    print("You WON !")
  elif(your_choice == 1 and computer_select == 0):
    print("You WON !")
  elif(your_choice == 1 and computer_select == 2):
    print("You Loose")
  elif(your_choice == 2 and computer_select == 0):
    print("You Loose")
  elif(your_choice == 2 and computer_select == 1):
    print("You WON !")
  else :
   print("Do not provide invalid choices")
