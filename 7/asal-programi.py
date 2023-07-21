# 2 ile 50 aralığındaki sayilarin asal olup olmadigini bulan programdir...

ilk_sayi = 2
son_sayi = 50

mevcut_sayi = ilk_sayi

while  mevcut_sayi <= son_sayi :
    mevcut_bolen =2
    mevcut_sayi_asal_mi = True
    while mevcut_bolen < mevcut_sayi :
        if mevcut_sayi % mevcut_bolen == 0 :
            mevcut_sayi_asal_mi = False
            break
        mevcut_bolen = mevcut_bolen +1
    if mevcut_sayi_asal_mi == True :
        print(mevcut_sayi, "asaldir.")
    else :
        print (mevcut_sayi, "asal degildir.")
    
    mevcut_sayi = mevcut_sayi +1


print ("Islem bitti.")
