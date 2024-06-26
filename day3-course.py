# day 3 control flow and logical operators
# exercise 1
print("===============================")
print("Welcome to the rollercoaster!")
print("===============================\n")

# Prompt the user to input their height in centimeters
height = int(input("What is your height in cm? "))

# Initialize the variable to keep track of the bill
bill = 0

# Check if the height is greater than 120 cm to determine if the person can ride the rollercoaster
if height > 120:
    # If the height is sufficient, inform the user that they can ride the rollercoaster
    print("You can ride the rollercoaster")
    
    # Prompt the user to input their age
    age = int(input("What is your age? "))
    
    # Determine the ticket price based on the age of the rider
    if age <= 12:
        # If the age is 12 or below, assign the child ticket price and update the bill
        print("Child tickets are $5")
        bill += 5
    elif 12 < age <= 18:
        # If the age is between 12 and 18 (inclusive), assign the youth ticket price and update the bill
        print("Youth tickets are $7")
        bill += 7
    elif 40 <= age <= 55:
        print("Life is gonna be alright, enjoy this free ride")
    else:
        # For ages above 18, assign the adult ticket price and update the bill
        print("Adult tickets are $12")
        bill += 12

    # Ask the user if they want a photo taken and adjust the bill accordingly
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    # Print the final bill
    print(f"Your final bill is ${bill} ")
else:
    # If the height is not sufficient, inform the user that they cannot ride the rollercoaster
    print("Sorry, you have to grow taller before you can ride.")

# exercise 2
print("===============================")
print("Odd and even number checker")
print("===============================")
# Which number do you want to check?
number = int(input("Please enter a number = "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.\n")
else:
  print("This is an odd number.\n")

# exercise 3
print("===============================")
print("BMI calculator V.2")
print("===============================")
# Enter your height in meters e.g., 1.55
height1 = float(input("What is your height ?\n"))
# Enter your weight in kilograms e.g., 72
weight = float(input("What is your weight ?\n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height1 ** 2
bmi = float("{:.2f}".format(bmi))
if bmi < 18.5:
  print(f'Your BMI is {bmi}, you are underweight.\n')
elif bmi < 25:
  print(f'Your BMI is {bmi}, you have a normal weight.\n')
elif bmi < 30:
  print(f'Your BMI is {bmi}, you are slightly overweight.\n')
elif bmi < 35:
  print(f'Your BMI is {bmi}, you are obese\n')
else:
  print(f'Your BMI is {bmi}, you are clinically obese\n')

#exercise 4 - leap year calculator
print("===============================")
print("Leap year calculator")
print("===============================")

# Which year do you want to check?
year = int(input("Please enter a year = "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Check if the year is divisible by 4
if year % 4 == 0:
    # If it is, further check if it's not divisible by 100
    if year % 100 == 0:
        # If not divisible by 100, it's a leap year unless divisible by 400
        if year % 400 == 0:
            # If divisible by 400, it's a leap year
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
    
#exercise 5 Pizza order
print("\n===============================")
print("Leap year calculator")
print("===============================")
print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N : ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N : ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"Your final bill is: ${bill}")

# exercise 6 - love calculator
print("\n===============================")
print("Love Calculator")
print("===============================")
print("The Love Calculator is calculating your score...")

name1 = input("Whats is your name ?\n") # What is your name?
name2 = input("What is your partner name?\n") # What is their name?

# Write your code below this line 👇
combined_names = name1 + name1
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and pizza.")
elif( score >= 40 and score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

print("\n\n")
# day 3 final project - mini choice games
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
print("You are at a crossroads. where do you want to go?")
direction = input("Type 'left' or 'right'\n")
lower_direction = direction.lower()
if lower_direction == "left":
          action = input('you\'ve come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat. Type "swim" to swim across. \n')
          lower_action = action.lower()
          if lower_action =="wait":

            door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ")
            lower_door = door.lower()
            if lower_door == "red":
                      print("It's a room full of fire. Game Over.")
            elif lower_door == "yellow":
                      print("You found the treasure! You Win!")
            elif lower_door == "blue":
                      print("Ther is a beast in the room. Game Over.")
          else:
                    print("You got attacked by an angry trout. Game Over.")
          
else:
          print("Falls into a hole. Game Over.")
          