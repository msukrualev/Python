saying = "Don't panic!"

# Bir objenin veri tipini başka bir veri tipne dönüştürmek için ;
# dönüştüreceğimiz veri tipinin ismiyle aynı isimde methodu kullanırız :
# Örneğin yukarıdaki string veriyi "list" e dönüştürelim :

letters = list(saying)

print(letters)
# letters isimli listin şöyle olduğu görülür :
# ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']
# yani string verideki her bir karakteri elemanı olarak aldı.

print(letters[0], '\n', letters[3], '\n', letters[6], '\n', letters[-1], '\n', letters[-3])

# listin bir elemanını başka bir variable'a atayabiliriz :

first = letters[0]

last = letters[-1]

# Slicing :

# Syntax ;  my_list[ start : stop : step ]
# start ; başlangıç indexi
# stop ; bitiş indexi -dahil değildir-
# step ; indexler alınırken artış miktarıdır.

# start eksik olduğunda, varsayılan değeri 0'dır.
# stop eksik olduğunda, liste için izin verilen maksimum değeri alır.
# step eksik olduğunda varsayılan değeri 1'dir.

print(letters[0:12])  # son index numarası 11 olduğu için stop'a 12 girdik, stop yani 12 dahil değildir.
                      # Bu yüzden en son 11 nolu indexi alır.

print(letters[0:10:3])

print(letters[3:])

print(letters[:10])

print(letters[::2])

print(letters[-6:])

print(letters[-1:])

print(letters[::-1])

print(letters[::-1])

print(letters[10:3:-1])