# W3Schools Python3 Tutorial
# Pt 2: Data Types, Numbers, Casting, and String Intro, Slicing Strings, and  # Modifying Strings


# Python has the following data types built-in by default, in these categories:
# Text Type: str
# Numeric Types: int, float, complex
# Sequence Types: list, tuple, range
# Mapping Type:	dict
# Set Types: set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

# Python Numbers

# Int (integer) is a whole number, positive or negative, without decimals,
# of unlimited length.

# Float is a number containing one or more decimal places. They can also be
# scientific numbers with an 'e' to indicate the power of 10.
x = 35.5
y = 12e4
z = 47E3

# Complex numbers are an extension of the familiar real number system in which all numbers are expressed as a sum of a real part and an imaginary part. ... Python has built-in support for complex numbers, which are written with this latter notation; the imaginary part is written with a j suffix,
# e.g., 3+1j.

x = 3+5j

# Complex numbers cannot be converted into another number type.

# RANDOM NUMBERS
# Python has a module called 'random' that can be used to generate (pseudo)-random numbers.

import random  
print(random.randrange(1, 20))

# MULTILINE STRINGS must use triple quotes, and can be assigned to variables.

# STRINGS ARE ARRAYS
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

a = 'supercalifragilisticexpialidocious'
print(a[1])

# Since strings are arrays, we can loop through a string's characters.

print("This sh*t is bananas!")
for x in 'bananas':
  print(x)


# Get the length of a string with len()

# To check if a certain phrase or character is present in a string, we can use the keyword in. Conversely, we can check for its absence with 'not in'.

txt = "The best things in life are free!"
print("free" in txt)

# SLICING STRINGS
# Specify the start index and end index (not inclusive), separated by a 
# colon, to return a part of the string.

b = "that darn cat"
print(b[2:9])

# To start at the first character, leave out the start index.

print(b[:9])

# To go all the way to the end, leave out the end index.

print(b[5:])

# To start the slice from the end of the string, use negative indices.
print(b[-7:-2])

# STRING MODIFICATIONS
# Python has built-in methods to modify strings.

mercury = "Is this the real life? Is this just fantasy?"

print(mercury.upper())
print(mercury.lower())

# remove whitespace before or after actual text with strip()

styx = "           I'm sailing away...                    "
print(styx.strip())

# replace() swaps a string for another string

a = "Hello world!"
print(a.replace("H", "J"))

# split() returns a list of substrings split at the specified separator

monty_python = "Spam, sausage, Spam, Spam, Spam, bacon, Spam, tomato and Spam"
print(monty_python.split(","))