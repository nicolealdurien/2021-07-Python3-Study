# W3Schools Python3 Tutorial
# Pt 3: String Concatenation/Formatting/Methods/Escape Characters, Booleans, 
# Arithmetic/Assignment/Comparison/Logical/Identity Operators 

a = "Robert"
b = "Plant"
zeppelin = a + " " + b
print(zeppelin)

# format() method can be used to insert numbers into strings where 
# placeholder curly braces {} have been left

x = 99
txt = "{} bottles of beer on the wall..."
print(txt.format(x))

# format() takes an unlimited number of arguments, and fills data into
# placeholders from left to right. You can also specify numbers within the
# placeholders to override the left-to-right order.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay ${2} for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# ESCAPE CHARACTERS
# To inserrt illegal characters in a string, they must be
# preceded by a backslash (\).

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# Other escape characters include the single quote, backslash, and new line
# (\n), among others.

# STRING METHODS
# There are a host of built-in methods you can use on strings. Here are just
# a few: capitalize(), startswtith(), title(), isalpha()


# BOOLEANS

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# None and False also evaluate to False.

# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Functions can return a Boolean and this answer can be used to execute
# other code:

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

# OPERATORS
# One operator unique to Python 3 is the // operator for floor division (that
# is, lopping off decimals instead of rounding).

# IDENTITY OPERATORS
# Compare if 2 variables point to the same object with the same memory 
# location

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("Is Exercise")
print(x is z)   # returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)  
# 'is' is not '==', they're the same value and data type, but not the same object