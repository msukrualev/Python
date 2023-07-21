"""
m = 0
for x in range(1,4):                
    for y in range(1,3):   
        m = m + 1
print (m)
"""
# x= 1 iken  y =1  : m =1   m = 0+1 m =1
#  x= 1 iken  y =2  : m =2
# x= 2 iken  y =1 : m =3
# x= 2 iken  y =2: m =4


m = 0

for x in range (1,3):
   k = 0
   for y in range (-2,0):
      k = k + y
      m = m + k
print (m)

# x =1 iken ;  k= 0
#             y = -2 iken ; k= 0 + (-2) = -2, m = 0 + (-2) = -2

# x =1 iken ; y = -1 iken ; k = -2 + -1 = -3,  m= -2 + -3 = -5

# x =2 iken ; k = 0 
#             y = -2 iken ; k = 0 + -2 = -2,  m = -5 + -2 = -7
# x =2 iken ; y = -1 iken ; k = -2 + -1 = -3 , m = -7 + -3 = -10        


