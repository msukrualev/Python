# 1'den 1001'e kadar her üçüncü sayının toplamını (hem 1 hem de 1001 dahildir) yazdıran
# while döngüsünü kullanan bir program yazın

x =1
count = 0

while x <= 1001 :         # 1 + 4 + 7 +.........1001
    count = count + x     # count = 0 +1 = 1      count = 1 + 4 = 5 
    x = x+3

print(count)