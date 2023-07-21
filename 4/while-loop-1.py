# 1'den 101'e kadar 5'e bölünebilen sayıların toplamını ekrana yazdıran bir program yazınız. 
# ( 1 ve 101 dahildir) (While döngüsü kullanın)

x = 0
count = 0

while x <= 101 :
    if x % 5 ==0:
        count = count+x   # x = 5 count = 0 + 5
    x = x+1
    
print (count)