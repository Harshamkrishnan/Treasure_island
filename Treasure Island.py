#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first_direction = input("You are at a cross road. Where do you want to go next? left,right or straight\n")
first_direction_lower = first_direction.lower()

if first_direction_lower == "straight" :
  print("!!!!You fell into a hole!!!! GAME OVER!!!")
elif first_direction_lower == "right" :
  print("You enter at lion's cave!!! Game over!!")
elif first_direction_lower == "left" :
  first_choice = input("Now you're at a river shore. Type 'wait' if you want to wait for a boat or type 'swim' if you want to swim!!\n")
  first_choice_lower = first_choice.lower()
  
  if first_choice_lower == "wait" :
    second_choice = input("Okay!!! You managed to reach infront of an old abandoned building!! if you want to go upstairs type 'Go up' if you want to go to the ground floor type 'go down'\n")
    second_choice_lower = second_choice.lower()
    
    if second_choice_lower == "go up" :
      third_choice = input("You can see three doors with colors green,blue and yellow. Which door would you want to choose?\n")
      third_choice_lower = third_choice.lower()
      
      if third_choice_lower == "blue" :
        print("!!!You fell into a well!!! GAME OVER!!!")
      elif third_choice_lower == "green" :
        print("!!!You enter to a room full of snakes!!! GAME OVER!!!")
      else:
        print("CONGRATULATIONS!!! YOU FOUND THE TREASURE!!!")
    else:
      fourth_choice = input("You see two doors with colors red and green. which one you want to choose?\n")
      fourth_choice_lower = fourth_choice.lower()

      if fourth_choice_lower == "red":
        print("!!!You enter to a room full of fire!!! GAME OVER!!!")
      else:
        print("!!!You enter to a room full of snakes!!!!! GAME OVER!!!")
  else:
    print("I appreciate your bravery!!! but also sorry that a crocodile caught you!!! GAME OVER!!!!")
else:
  print("!!!Wrong choice!! GAME OVER!!!")


# In[ ]:




