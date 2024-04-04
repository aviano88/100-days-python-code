# Write your code below this line 👇
#Exercise 1
print("Hello World!\nHello World!\nHello World!")
print("Hello" + " " + "Angela\n")

#Exercise 2
# input() will get user input in console
# Then print() will print the word "Hello" and the user input
name = input("what is your name?\n")
length = len(name)
print("Hello " + name + "!")
print("letter counter = " + str(length) + "\n")

#Exercise 3
# 🚨 Don't change the code below 👇
#switching variables using temporary variables
print("VV_Swtiching Machine_VV")
varA = input("a: ")
varB = input("b: ")
temp = varA
varA = varB
varB = temp

print("VV_switching result_VV\n" + "a: " + varA + "\n" +"b: " + varB)

#First Project : Band Name Generator
#1. Create a greeting for your program.
print("Welcome to the Band Name Generator")
#2. Ask the user for the city that they grew up in.
city = input("what's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("what's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("your band name could be " + city + " " + pet)
#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end