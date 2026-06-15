# Chapter 1 - Variable & Data Types
## What is a Variable?
A variable is a container that stores a value in memory.
You give it a name, and Python remembers the value for you.

### Syntax
```code
variable_name = value
```
### Rules for Naming Variables
- Must start with a letter or undscore
- Cannot start with a number
- No spaces allowed ( use underscore insted)
- Case sensitive (name and Name are different)

### Examples :
```code
name        - valid     
1name       - invalid
first_name  - valid     
first name  - invalid
```

---

## Data Types - The 6 You Must Know
| Data Type | Keyword | Description | Example |
|-----------|---------|-------------|---------|
| Integer | `int` | Whole numbers (no decimal point) | `age = 20` |
| Float | `float` | Numbers with decimal points | `price = 99.99` |
| String | `str` | Text enclosed in quotes | `name = "Rahul"` |
| Boolean | `bool` | Represents `True` or `False` | `is_student = True` |
| List | `list` | Stores multiple items in order | `marks = [85, 90, 78, 92]` |
| Dictionary | `dict` | Stores data as key-value pairs | `student = {"name": "Rahul", "age": 20}` |

---

## type() Function
Tells you or returns what data type a variable is.
ex :
```python
x=42
print(type(x)) #<class 'int'>

y="hello"
print(type(y)) #<class 'str'>
```

---

## Type Conversion
Converting one type to another.
```code
int("42")   -   42      (string to integer)
str(42)     -   "42"    (integer to string)
float(42)   -   42.0    (integer to float)
int(3.9)    -   3       (float to int, decimal removed)
```
---

## input() Function
Taking input from user. it always return a string.

```python
name = input("Enter your name :")
age = int(input("Enter your age :"))
```
Note : input() always give a string.
if you need number, convert it with int() or float()

---

## print() Function
Displaying output
```python
print("hello") # display string
print(name) # display variable value
print("My name is ",name,"and i am ",age," years old") # display string with variable value. comma used for separet string & varibale.
print(f"My name is {name} and i am {age} years old") # display str & var value using f-string.
```
---
## My Key Takeaways

1. Variables store data in memory and can be reused throughout a program.
2. Python has different data types such as int, float, str, bool, list, and dict.
3. input() always returns a string, so type conversion may be needed when working with numbers.

## Questions I Still Have

1. When should I use a list instead of a dictionary?
2. What happens if I try to convert invalid text to an integer (e.g., int("hello"))?

## Practice Task : 
```python 

# Chapter 1 Practice
# ==================

# Drill 1 — Create one variable of each data type
# Write your own. Don't copy mine.
# integer, float, string, boolean
# Print each one with its type using type()



# Drill 2 — Type Conversion
# Take this string: "25"
# Convert it to integer and add 10
# Print the result



# Drill 3 — User Input
# Ask the user for their name and age
# Print: "Hello [name], you are [age] years old"
# Make sure age is stored as integer, not string



# Drill 4 — F-strings
# Store your name, age, and course in variables
# Print one sentence using f-string that includes all three



# Drill 5 — Think about this
# What happens if you do this:
# age = input("Enter age: ")
# print(age + 10)
# Try it. See the error. Understand why. Fix it.
```
## Date Completed
15 June 2026