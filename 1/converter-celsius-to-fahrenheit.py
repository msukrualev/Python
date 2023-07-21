# Girilen Celsius değerini Fahrenheit'a dönüştüren programdır.
# 1. Celsius değerini gir
# 2. Girilen Celsius değerini 9 ile çarp.
# 3. İkinci adımdan alınan sonucu 5'e böl.
# 4. Üçüncü adımın sonucuna 32 ekle.
# 5. DÖrdüncü adımın sonucunu ekrana yazdır.

celsius_degeri = int(input("Celsius degerini girin : "))

#celsius_degeri = celsius_degeri*9

#celsius_degeri = celsius_degeri/5

fahrenheit_degeri = (celsius_degeri*9)/5 + 32

print("Girilen sıcaklığın Fahrenheit değeri", fahrenheit_degeri)