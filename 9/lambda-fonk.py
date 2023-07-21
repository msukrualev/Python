# Syntax

# lambda arguments : expression
"""
x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)  # lambda a : a * 2

print(mydoubler(11))
"""
# Local Scope

def myfunc():
  x = 300
  print(x)


# global Scope

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# Local Scope tan global scope'a çevirme

def myfunc():
  global x 
  x= 300
  print(x)


myfunc()

print(x)