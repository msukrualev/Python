# Kullanıcıdan 1 ile 7 arasında pozitif bir tamsayı isteyen 
# (Kullanıcının 1'den 7'ye kadar herhangi bir sayı girebileceğini varsayalım) 
# ve bu sayıya karşılık gelen haftanın gününü tamamı büyük harflerle yazdıran 
# bir program yazınız. Haftanın gününün PAZARTESİ'den başladığını varsayalım. 
# Örneğin: kullanıcı şunu girerse:  2
# programınız SALI yazdırsın...

hafta_gunleri = ['PAZARTESİ','SALI','ÇARŞAMBA','PERŞEMBE','CUMA','CUMARTESİ','PAZAR']
user_input = int(input())
print(hafta_gunleri[user_input-1])