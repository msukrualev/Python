"""
def my_fun( a ):
    return a*2

my_fun( 2 )  #   Bu satırın sonucu 4 değer olarak

# print(    my_fun( 2 )       )

# b = my_fun( 2 )
# print(b)

# print(   my_fun(2) + my_fun(3)     )

# print(   my_fun( my_fun(2)  )     )

def hello() :
    print("Hello there")

# hello()
print(hello())  # None



def hello() :
    print("Hello there")


for k in range(1,5) :
    hello()


#Bir sayıyı argument olarak kabul eden ve o sayının karesini döndüren bir fonksiyon yazınız. 
#Örneğin, fonksiyona verilen sayı 5 ise, fonksiyon 25 döndürmelidir.
def my_func ( x ) :
    return x**2


# my_func(5)  # 25 değer olarak dönmüş olacak

print(my_func(5))
"""
# pozitif bir 'r' sayısını dairenin yarıçapı olarak kabul eden (argument olarak alan) ve dairenin alanını hesaplayıp
# değer olarak geri döndüren bir fonksiyon yazın. Pi değerini 3.14 olarak kullanın

def daire_alani( r ) :
    return 3.14*r*r

daire_a = daire_alani( 2 )

print(daire_a)