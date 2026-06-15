# Chapter 1 Practice
# ==================

# Drill 1 — Create one variable of each data type
# Write your own. Don't copy mine.
# integer, float, string, boolean
# Print each one with its type using type()

print(" Drill 1 : ")
print("=========================================")
name="kalpesh"
year=2026
isPass=True
perc=80.99
print(name," ",type(name))
print(year," ",type(year))
print(isPass," ",type(isPass))
print(perc," ",type(isPass))
print("=========================================")

# Drill 2 — Type Conversion
# Take this string: "25"
# Convert it to integer and add 10
# Print the result

print(" Drill 2 : ")
print("=========================================")
print("result : ",int("25")+10)
print("=========================================")

# Drill 3 — User Input
# Ask the user for their name and age
# Print: "Hello [name], you are [age] years old"
# Make sure age is stored as integer, not string

print(" Drill 3 : ")
print("=========================================")
name=input("Enter your name :")
age=int(input("Enter your age :"))
print("Hello ",name," you are ",age," years old")
print("=========================================")

# Drill 4 — F-strings
# Store your name, age, and course in variables
# Print one sentence using f-string that includes all three

print(" Drill 4 : ")
print("=========================================")
course="BCA"
print(f"My name is {name}, I am {age} years old and I am doing {course} course.")
print("=========================================")

# Drill 5 — Think about this
# What happens if you do this:
# age = input("Enter age: ")
# print(age + 10)
# Try it. See the error. Understand why. Fix it.

print(" Drill 5 : ")
print("=========================================")
ages=input("Enter age :")
print(ages + 10) # This will give an error because age is a string and we cannot add an integer to a string
print("=========================================")