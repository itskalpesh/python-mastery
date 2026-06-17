# ================================
# Chapter 2 — Strings
# ================================

# --- Drill 1: Indexing & Slicing ---
# Store your full name in a variable
# Print: first character, last character,
# first 3 characters, everything after index 3
print("Drill 1 :")
print("==========================================")
name = "Kalpesh Kurbetti"
print("1st char : ",name[0])
print("last char : ",name[-1])
print("1st 3 char : ",name[:4])
print("after index 3 : ",name[4:])
print("==========================================\n")

# --- Drill 2: String Methods ---
# Store this exact string:
# text = "  python is GREAT for beginners  "
# Print it: uppercased, lowercased,
# stripped of spaces, with "GREAT" replaced by "perfect"

print("Drill 2 :")
print("==========================================")
text = "  python is GREAT for beginners  "
print("Uppercase : ",text.upper())
print("lowercase : ",text.lower())
print("Replace & strip : ",text.replace("GREAT","perfect").strip())
print("==========================================\n")

# --- Drill 3: Split & Join ---
# Split this sentence into a list of words:
# sentence = "I am becoming a Python developer"
# Print the list
# Print how many words are in it
# Join it back into a string using "-" instead of spaces
# Expected: "I-am-becoming-a-Python-developer"
print("Drill 3 :")
print("==========================================")
sentence = "I am becoming a Python developer"
words=sentence.split()
print("list of words : ",words)
print("cound words : ",len(words))
print("join with '-' : ","-".join(words))
print("==========================================\n")

# --- Drill 4: String Analysis ---
# Ask user to enter any sentence
# Print:
#   - Total characters (including spaces)
#   - Total characters (without spaces)
#   - The sentence in UPPERCASE
#   - How many times the letter 'a' appears (lowercase)
#   - Whether the sentence starts with "I"

print("Drill 4 :")
print("==========================================")
msg=input("enter sentence : ")
print(len(msg))
print(len(msg.replace(" ","")))
print(msg.count("a"))
print(msg.startswith("I"))
print("==========================================\n")

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

print("Drill 5 :")
print("==========================================")
fname=input("enter full name : ")
print(len(fname.replace(" ","")))
print(fname[::-1])
print(".".join(word[0] for word in fname.split())+".")
print("==========================================\n")
