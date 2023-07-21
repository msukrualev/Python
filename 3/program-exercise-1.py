# 1. Program :
# Kullanıcıdan yaşını yıl cinsinden girmesini isteyen 
# (kullanıcının pozitif bir tamsayı girdiğini varsayalım) 
# ve kullanıcının gün cinsinden kaç yaşında olduğunu hesaplayan 
# ve ekrana yazdıran bir program yazınız. 
# Bir yılda 365 gün olduğunu varsayalım.

age = int(input())
age_days = age*365
print("You are", age_days, "days old")

# 2. Program :
#Kullanıcıdan 'x' tamsayısını isteyen 
# ve aşağıdaki ifadeyi değerlendirdikten sonra 
# y'nin değerini yazdıran bir program yazın:
# y = x^2 - 12x + 11    (x^2 ifadesi x'in karesi anlamına geliyor.)

x = int(input())
y = x*x - 12*x + 11
print(y)

