# day 2 - Data types and type casting

# Exercise 1 - math operation and type casting
# Taking input from the user
two_digit_number = input("Please enter 2 digits number = ")
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇

# Extracting the first and second digits from the input string and converting them to integers
firstNumber = int(two_digit_number[0])
secondNumber = int(two_digit_number[1])
# Performing addition of the two digits
result = firstNumber + secondNumber

# Displaying the result
print("the result of " + str(firstNumber) + " + " + str(secondNumber) + " equals to " + str(result) +"\n")

# Exercise 2 - BMI calculator

# Taking input for height in meters
height = input("please input your height in meters = ")

# Taking input for weight in kilograms
weight = input("please input your weight kilograms = ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Converting height and weight inputs to float and integer respectively
height = float(height)
weight = float(weight)
# Calculating BMI using the formula: weight / (height * height)
bmi = weight / (height ** 2)
# Displaying the calculated BMI
print("your bmi are " + str(bmi))
#print using f-string
print(f"your bmi are {bmi}\n")

# exercise 3 - week left until 90 years

age = input("enter current age = ")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
ageLeft = (90 - int(age)) * 52
print(f"You have {ageLeft} weeks left.\n")

# Day 2 final project day calculator
# Explanation of the code:
# The purpose of this code is to calculate the amount each person needs to pay after splitting the bill, including tip, among a certain number of people.

# Welcome message
print("Welcome to the tip calculator.\n")

# Taking input from the user: total bill amount
bill = input("What was the total bill? \n$")

# Taking input from the user: tip percentage (10%, 12%, or 15%)
tip = input("How much tip would you like to give? 10, 12, or 15?\n")

# Taking input from the user: number of people to split the bill
person = input("How many people to split the bill?\n")

# Converting input strings to appropriate data types
bill_as_float = float(bill)
tip_as_int = int(tip)
person_as_int = int(person)

# Converting tip percentage to a decimal
tip_as_percent = tip_as_int / 100

# Calculating the total tip amount
total_tip_amount = bill_as_float * tip_as_percent

# Calculating the total bill amount including tip
total_bill = bill_as_float + total_tip_amount

# Calculating the amount each person should pay
bill_per_person = total_bill / person_as_int
final_amount =round(bill_per_person, 2)
final_amount ="{:.2f}".format(bill_per_person)
# Displaying the amount each person should pay, rounded to 2 decimal places
print(f"Each person should pay: ${final_amount}")

