# Chapter 2 - Strings

## What is a String?
Astring is a sequence of characters inside quotes.
Single quotes, double quotes - both work.

```python
name = "Kalpesh"
city = "Nipani"
msg = "I am learning Python"
```
---
## 1. String Indexing
Every character in a string has a position number called an index. Index start at 0.
```python
name = "Kalpesh"
print(name[0])  # K
print(name[1])  # a
print(name[-1]) # h -> last character
print(name[-2]) # s -> second from last
```
---
## 2. String Slicing
Extract a position of a string.
```python
name = "Kalpesh"
print(name[0:3])    # Kal  -> 0, 1, 2 (3 not included)
print(name[2:5])    # lpe 
print(name[ :4])    # Kalp -> from start to index 3
print(name[4: ])    # esh  -> from index 4 to end
```
---
## 3. String Length
```python
name = "Kalpesh"
print(len(name))    # 7
```
---
## 4. String Methods - The Most Important Ones
```python
text = " hello world "
text.upper()                    # " HELLO WORLD "    <-  all uppercase
text.lower()                    # " hello world "    <-  all lowercase
text.strip()                    # "hello world"      <-  removes spaces from both ends
text.replace("world","python")  # " hello python "   
text.split()                    # ["hello", "world"] <-  splits into a list
```
```python
sentence = "Python is awesome"
sentence.startswith("Python")    # True
sentence.endswith("awesome")    # True
sentence.find("is")             # 7     <-  index where "is" starts
sentence.count("0")             # 2     <-  how many times "o" appears
```
---
## 5. String Checking Methods
```python
"hello123".isalpha()            # False -> not all letters
"hello".isalpha()               # True  -> all letters
"123".isdigit()                 # True  -> all digits
"hello".isdigit()               # False
"Hello World".idtitle()         # True  -> each word starts with capital
```
---
## 6. String Joining
Opposite of split. Joins a list of words into one string.
```python
words = ["Python", "is", "awesome"]
result = " ".join(words)
print(result)                   # "Python is awesome"
```
## 7. F-String (Formatted Strings)
The cleanest way to insert variable into strings.
```python
name = "Kalpesh"
course = "BCA"
sem = 5
print(f"My name is {name}, i am in {course} Semester {sem}")
# My name is Kalpesh, i am in BCA Semester 5
```
You can also do math inside f-strings :
```python
a = 10
b = 3
print(f"{a} divide by {b} is {a/b:.2f}")
# 10 divide by 3 is 3.33 <- .2f means 2 decimal places
```
---
## 8. Multiline Strings
```python
msg = """ Welcome to python chapter 2.
keep going."""
print(msg)
```
## 9. Escape Characters

| Escape | Meaning |
|---------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\"` | Double quote |
| `\'` | Single quote |
| `\\` | Backslash |

### Example

```python
print("Hello\nWorld")
print("Name\tAge")
print("He said \"Hello\"")
print('I\'m learning Python')
print("C:\\Users\\Kalpesh")
```
A small note : `\'` is only needed inside a single-quoted string, and `\"` is only needed inside a double-quoted string.<br>
example :
```python
print("I'm learning Python") # no escape needed
print('He said "Hello"') # no escape needed
```

## Key Takeaways

1. Strings are sequences of characters and can be accessed using indexing and slicing.
2. String methods like upper(), lower(), strip(), split(), and replace() make text manipulation easy.
3. F-strings provide a clean and readable way to format output using variables.

## Questions I Still Have

1. When should I use slicing instead of string methods?
2. What are some real-world uses of f-strings and string manipulation?

## Practice Task :
```python
# ================================
# Chapter 2 — Strings
# ================================

# --- Drill 1: Indexing & Slicing ---
# Store your full name in a variable
# Print: first character, last character,
# first 3 characters, everything after index 3



# --- Drill 2: String Methods ---
# Store this exact string:
# text = "  python is GREAT for beginners  "
# Print it: uppercased, lowercased,
# stripped of spaces, with "GREAT" replaced by "perfect"



# --- Drill 3: Split & Join ---
# Split this sentence into a list of words:
# sentence = "I am becoming a Python developer"
# Print the list
# Print how many words are in it
# Join it back into a string using "-" instead of spaces
# Expected: "I-am-becoming-a-Python-developer"



# --- Drill 4: String Analysis ---
# Ask user to enter any sentence
# Print:
#   - Total characters (including spaces)
#   - Total characters (without spaces)
#   - The sentence in UPPERCASE
#   - How many times the letter 'a' appears (lowercase)
#   - Whether the sentence starts with "I"



# --- Drill 5: The Real Challenge ---
# Ask user to enter their full name
# Print:
#   - Total characters in their name (without spaces)
#   - Their name reversed
#   - Their initials (first letter of each word)
# Example:
#   Input:  "Kalpesh Patel"
#   Output: Characters: 12
#           Reversed: lelaP hseplak  (the whole string reversed)
#           Initials: K.P
```

## Date Completed
27-07-2025