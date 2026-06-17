# Chapter 3 - Lists
## What is a List?
A list is an ordered collection that can hold multiple values.<br>
Created with square brackets.Values can repeat, & can change.
```python
numbers = [10, 20, 30, 40, 50]
names = ["Abhi", "Kalpesh", "Sham"]
mixed = [1, "hello", True, 3.14]        # lists can mix types
```
---
## 1. Indexing - Same Rules as Strings
```python
fruits = ["apple", "banana", "mango", "grapes"]
print(fruits[0])    # apple
print(fruits[2])    # mango
print(fruits[-1])   # grapes    -> last item
```
---
## 2. Slicing - Same Rules as Strings
```python
fruits = ["apple", "banana", "mango"]
print(fruits[1:3])  # ['banana', 'mango']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[2:])   # ['banana', 'mango']
```
---
## 3. Changing a List (Lists are mutable)
Strings cannot change after creation, list can.
```python
fruits=["apple", "banana"]
fruits[1]="orange"
print(fruits)       # ['apple', 'orange', 'banana']
```
---
## 4. Adding Items
```python
fruits = ["apple", "banana"]

fruits.append("mango")
print(fruits)

fruits.insert(1,"kivi")
print(fruits)
```
---
## 5. Removing Items
```python
fruits=["apple", "banana", "mango"]

fruits.remove("banana")            # remove by value
print(fruits)

fruits.pop()                       # removes last item, also returns it.
fruits.pop(0)                      # remove item at index 0.

del fruits[0]                      # remove by index, no return value.
```
---
## 6. List Functions
```python
num = [5, 2, 9, 1, 7]
len(num)                # 5             ->
max(num)                # 9             ->
min(num)                # 1             ->
sum(num)                # 24            ->
sorted(num)             # [1,2,5,7,9]   ->
num.sort()              # sort original list permanently
num.reverse()           # reverse original list permanently
```
## 7. Checking Membership
```python
fruits=["apple", "banana", "mango"]
print("banana" in fruits)          # True
print("kiwi" in fruits)            # False
print("kiwi" not in fruits)        # True
```
## 8. Looping Through a list
```python
fruits = ["apple", "banana", "mango"]

for f in fruits :
    print(f)

# with index using enumerate()

for index, f in enumerate(fruits):
    print(index,f)

# 0 apple
# 1 banana
# 2 mango
```
---
## 9. List Comprehension (Importnt-Used Everywhere)
A shorter way to create a list using a loop in one line.
```python
# Traditional Way
sqr=[]
for n in range(1,6):
    sqr.append(n*n)
print(sqr)          # [1,4,9,16,25]

# List Comprehension way - same result
sqr=[n*n for n in range(1,6)]
print(sqr)          # [1,4,9,16,25]

# With a condition
nums = [1,2,3,4,5,6,7,8,9,10]
evens=[n for n in nums if n % 2 == 0]
print(evens)        # [2,4,6,8,10]
```
## 10. Nested Lists ( list inside a List)
```python
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0])        # [1,2,3]
print(matrix[0][1])     # 2
```

## Practice Task :
```python
# ================================
# Chapter 3 — Lists
# ================================

# --- Drill 1: Basic Operations ---
# Create a list of 6 numbers of your choice
# Print: the list, length, highest, lowest, sum, average



# --- Drill 2: Adding & Removing ---
# Start with this list:
# fruits = ["apple", "banana", "mango"]
# Add "kiwi" to the end
# Add "orange" at index 1
# Remove "banana"
# Print the final list after each step (4 prints total)



# --- Drill 3: THE Number Analyzer (Your Day 1 Problem) ---
# Take a list of numbers: [12, 7, 18, 3, 25, 9, 14, 6]
# Print:
#   - Highest number
#   - Lowest number  
#   - Average
#   - All even numbers (as a list)
#   - Count of even numbers
#   - All odd numbers (as a list)



# --- Drill 4: List Comprehension Practice ---
# Take this list: numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# Using list comprehension, create:
#   - A list of squares of all numbers
#   - A list of only numbers divisible by 3
#   - A list of numbers greater than 10



# --- Drill 5: The Real Challenge — Grade Analyzer ---
# marks = [45, 78, 92, 34, 67, 88, 23, 95, 56, 71]
# Print:
#   - Highest mark and lowest mark
#   - Average mark (rounded to 2 decimals)
#   - List of students who passed (marks >= 40)
#   - Count of students who passed
#   - List of students who failed (marks < 40)
#   - Highest mark's position in original list (use a method, not a loop)
```
## Date Completed
17-06-2025