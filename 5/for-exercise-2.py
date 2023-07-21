# Bir for döngüsü kullanarak, kullanıcıdan n tamsayısını yazmasını isteyen ve ardından 1'den n'ye kadar olan 
# tüm sayıların (hem 1 hem de n dahil) toplamını yazdıran bir program yazın.

y = int(input("Bir tam sayi giriniz :"))

toplam = 0

for k in range(1, y+1):
    toplam = toplam + k

print(toplam)