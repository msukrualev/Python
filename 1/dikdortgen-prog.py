# Bu program dikdörtgenin çevresi ve alanını hesaplar...

# input() methodu kullanıcıdan girdi almayı sağlar.
# Syntax ;  input(ekran_yazısı)

# yukseklik = input()   # input fonksiyonu klavyeden aldığı değeri string olarak döndürür. Sayı değil string '15' girmiş oldum.
yukseklik = int(input("Yükseklik değerini giriniz : "))   # int ; integer.  int() methodu içerisine girilen değeri integer'a dönüştürür.
genislik = int(input("Genişlik değerini giriniz : "))

alan = yukseklik*genislik
cevre = (yukseklik + genislik)*2

print("Dikdörtgenin alanı : ", alan)
print("Dikdörtgenin cevresi : ", cevre)

