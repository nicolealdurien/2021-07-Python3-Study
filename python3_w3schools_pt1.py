# W3Schools Python3 Tutorial
# Pt 1: Intro, Get Started, Syntax, Comments, and Variables

# Python Command Line
# Enter by typing 'python' (or 'python 3' on macs where 2.7 is preinstalled)
# so it knows which version you want. Exit by typing 'exit()'.

# Indentation: can use whatever number of spaces you want but it must be at least one.
# If you don't use the same number of spaces in teh same block of code,
# Python will throw an error.


# Python has no command for declaring a variable without assigning a value to it.

# Comments can be placed mid-line; Python will ignore the rest of the line.

print("Comments are cool.")  # See?

'''
For multi-line comments, you can either put a # at the start of each line, or use
triple quotes. The latter works because Python will ignore string literals that are
not assigned to a variable.
'''

# Variables do not need to be declared with any particular type and can even
# change type after they have been set.

x = 27           # x is type int
x = "Aragorn"    # x is now type str
print(x)


# CASTING

x = str(27)     # x will be '27'
y = int(27)     # y will be 27
z = float(27)   # z will be 27.0

# type() will give you a variable's data type

print(type(z))

# Strings can be declared with either single or double quotes.

# Variable names are case-sensitive. (age, Age, and AGE are 3 different variables.)

a = "Gandalf"
A = "Saruman"
print(a) 

# Variable names must start with a letter or underscore, and can contain only
# alpha-numeric characters and underscores.

# You can assign multiple variables in one line.

d, e, f, g = "Frodo", "Sam", "Merry", "Pippin"

print(d)
print(e)
print(f)
print(g)

# You can also assign the *same* value to multiple variables in one line.

h = i = j = "Bilbo"

print(h)
print(i)
print(j)

# If you have a collection of values in a list, tuple, etc, Python allows you to 
# extract the values into variables. This is called 'unpacking'.

fruits = ['apple', 'banana', 'cherry']

k, l, m = fruits

print(k)
print(l)
print(m)

# Variables created outside of a function are GLOBAL and can be used both 
# inside and outside of functions. Variables created inside a function are
# LOCAL and only used inside the function. To create a global variable inside
# a function you must use the 'global' keyword. 

x = "awesome"

def myfunc():
  x = "fantastic"
  global y
  y = "stupendous"
  print("Python is " + x)

myfunc()

print("Python is " + x)
print("Python is " + y)

# You must also use the 'global' keyword if you want to change a global variable
# from inside the function.

x = "say what"

def myfunc():
  global x
  x = "what?"

myfunc()

print("Python is " + x)