# Bir for döngüsü kullanarak 1'den 101'e kadar olan tüm çift sayıların toplamını ekrana yazdıran bir program yazınız.

toplam = 0

for x in range(1,102):
    if x%2 == 0 :
        toplam = toplam + x     # 0 + 2 + 4 + 6 +....

print(toplam)