# 
s = "Hello world"    # 0,1,2,3,10    0-10 
len_sonucu = len(s)  # len() methodu içerisine girilen değişkenin eleman sayısını döndürür.
                     # Burada s değişkeni 11 elemana sahip bir değişkendir, string bir değer tutuyor.
print("s stringinin son elemanı :", s[10])
print("s stringinin son elemanı :", s[-1])
print("len fonksiyonunun sonucu :", len_sonucu)
print("s stringinin son elemanına len ile ulaşalım :", s[len(s)-1])