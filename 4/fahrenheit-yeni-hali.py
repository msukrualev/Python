### Bir program yazmak istediğimizi düşünelim.
# Celsius cinsinden bir giriş sıcaklığı elde etmek için bunu Fahrenheit'e çevirin.
# Ardından sıcaklığı Fahrenheit olarak yazdırmak istiyoruz.
# Sonra 32 derecenin altındaysa "It is freezing." yazdırmak istiyoruz.
# 32 ile 50 derece arasındaysa "It is chilly." yazdırmak istiyoruz.
# 50 ile 90 derece arasındaysa "It's OK." yazdırmak istiyoruz.
# Ve 90 derecenin üzerindeyse, "It is hot" yazdırmak istiyoruz.

celsius_degeri = int(input("Celsius degerini girin : "))

fahrenheit_degeri = (celsius_degeri*9)/5 + 32

print("Girilen sicakligin Fahrenheit degeri", fahrenheit_degeri)

if fahrenheit_degeri < 32 :
    print("It is freezing.")
elif fahrenheit_degeri < 50 :
    print("It is chilly.")
elif fahrenheit_degeri < 90 :
    print("It's OK.")
else :
    print("It is hot")