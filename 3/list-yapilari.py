prices = []   # Boş bir list oluşturalım

temps = [ 32.0, 212.0, 0.0, 81.6, 100.0, 45.3 ]   # Float tipinde objeler tutan bir list oluşturalım

words = [ 'hello', 'world' ]   # Strin tipi veriler-objeler tutan bir list

car_details = [ 'Toyota', 'RAV4', 2.2, 60807 ]  # Farklı tiplerde objeler tutan bir list

# Şimdi "listleri tutan bir list" oluşturalım.
# Bunu yapabiliriz, çünkü list yapıları heterojendir, farklı türlerde objeler tutabilir.
# List de diğer veri tipleri gibi  bir veri tipidir.
# Öyleyse listlerin listi oluşturulabilir :

everything = [ prices, temps, words, car_details ]   
# Yukarıda tanımladığımız listleri eleman olarak alan "everything" isimli bir list oluşturduk.

# Önceden tanımlamadan doğrudan [] syntaxı ile listleri de eleman olarak verebiliriz :
 
odds_and_ends = [  [ 1, 2, 3],   ['a', 'b', 'c' ],  [ 'One', 'Two', 'Three' ]  ]

