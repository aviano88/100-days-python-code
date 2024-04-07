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
print("the result of " + str(firstNumber) + " + " + str(secondNumber) + " equals to " + str(result))

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