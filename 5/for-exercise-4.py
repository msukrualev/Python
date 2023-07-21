""" 
Kullanıcıdan 'n' girdisini isteyen (kullanıcının pozitif bir tamsayı girdiğini varsayalım) ve
 10^0'dan 10^n'ye kadar 10'luk bir üs dizisini ayrı satırlara yazdıran bir program yazın.
 Örneğin, 'n' 4'e eşitse, çıktı aşağıdaki gibi görünmelidir:
1
10
100
1000
10000

"""

n = int(input("Bİr sayi giriniz :"))

for x in range(0, n+1) :
    print(10**x)