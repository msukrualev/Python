"""
for char in "computer":
    print(char)



for char in "computer":
    if char == 'p':
        continue
    print(char)



for char in "computer":
    if char == 'p':
        break
    print(char)

print("break keywordu for'un disina atti...")



count = 20

for x in range(0,10) :
    count = count-1   # x= 0 iken count =19 , x=1 iken count = 18, x=2 count =17
    if x == 2 :
        break

print(count)




k = 1

while k < 15 :
    if k%7 ==0 :
        break
    k= k+2

print(k)



my_str = "university"

count =0

for char in my_str :
    if char == 'i':
        continue
    else :
        count = count +1

print(count)

"""