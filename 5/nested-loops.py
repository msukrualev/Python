# Bir sayinin asal olup olmadigini bulan programdir...

mevcut_sayi = 24

mevcut_bolen = 2

mevcut_sayi_asal_mi = True

while mevcut_bolen < mevcut_sayi :
    if mevcut_sayi % mevcut_bolen == 0 :
        mevcut_sayi_asal_mi = False
        break
    mevcut_bolen = mevcut_bolen + 1

    
if mevcut_sayi_asal_mi :
    print (mevcut_sayi, " asaldir")
else :
    print (mevcut_sayi, "asal degildir")

print ("Islem bitti.")