# Bir for döngüsü kullanarak, kullanıcıdan pozitif bir tamsayı olan n'yi yazmasını isteyen ve 
# ardından 1'den n'ye kadar olan tüm sayıların (hem 1 hem de n dahil) karelerinin toplamını yazdıran bir program yazın.

y = int(input("Bir sayi giriniz :"))

toplam = 0

for i in range(1, y+1):
    toplam = toplam + i**2

print(toplam)