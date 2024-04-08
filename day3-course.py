# day 3 control flow and logical operators
# exercise 1
print("===============================")
print("Welcome to the rollercoaster!")
print("===============================\n")

height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
  print("You can ride the rollercoaster")
  age = int(input("What is your age? "))
  if age <= 12:
    print("child tickets are $5")
    bill += 5
  elif 12 < age <= 18:
    print("youth tickets are $7")
    bill += 7
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    print("adult tickets are $12")
    bill += 12

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo =="Y":
    bill += 3

  print(f"Your final bill is ${bill} ")
else:
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