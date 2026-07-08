print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
go = input("Where do you want to go?\nleft or right")

if go == "left" or go == "Left":
    print("You arrive at the island unharmed.")
    next = input("Do you want to swim or wait for boat?")
    if next == "boat" or next == "Boat":
        print("There is a house with 3 doors.red,yellow and blue.")
        door = input("Which colour do you choose?")
        if door == "red" or door == "Red":
            print("you Burned by fire. Game Over.")
        elif door == "Yellow" or door == "yellow":
            print("You win the treasure")
        elif door == "Blue" or door == "blue":
            print("You are eaten by beasts.")
    elif next == "swim" or next == "Swim":
        print("You get attacked by an angry trout. Game over.")
elif go == "right" or go == "Right":
    print("game over")












