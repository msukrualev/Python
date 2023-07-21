# Kullanıcıdan pozitif bir tamsayı olan n yazmasını isteyen ve ardından n'nin faktöriyelini yazdıran
# while döngüsünü kullanan bir program yazın. Faktöriyel, 1'den n'ye (1 ve n dahil) kadar tüm sayıların
# çarpımı olarak tanımlanır. Örneğin 4'ün faktöriyeli 24'e eşittir. (çünkü 1*2*3*4=24)

y = input("Bir sayi giriniz :")

x = int(y)

count = 1
z=1

while z <= x :
    count = count *z
    z = z+1

print(count)