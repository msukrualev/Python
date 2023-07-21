"""
x = "university"

print(x[5:0:-2])

### STRING METHODLARI ::

## str.count( )
## Syntax ; str.count( value, start, end )
txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple")
# x = txt.count("apple", 10, 24)
x = txt.count("Ilove")
print(x)

## str.replace( )

#Syntax ; str.replace(old_value, new_value, count)

txt = "I like apples"

x = txt.replace("apples","flowers")

print(x)


txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")
y = txt.replace("one", "three", 2)
#print(x)

print(y)


## str.split( )

# string.split(separator, maxsplit)

txt = "welcome to the jungle"

x = txt.split()

print(x)


txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)



txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)
"""

txt = "apple#banana#cherry#orange"

# maxsplit parametresini 1 yaparsak, 1 kez böleceği için iki elemanlı bir list ortaya çıkar:

x = txt.split("#", 1)

print(x)

