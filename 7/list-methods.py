"""
vowels = [ 'a', 'e', 'i', 'o', 'u' ]

word  = "Milliways"

for letter in word :
    if letter in vowels :
        print(letter)

# length ()  objenin eleman sayisini dönduruyor

my_list = [ 'two', 5, ['one', 2 ]  ]

print( len(my_list))

# append() methodu :
# append() methodu bir list'in sonuna eleman eklemek için kullanılır.
# Syntax ;   list.append(elmnt)

my_list = []

my_list.append('a')

my_list.append('e')

my_list.append('i')

my_list.append('o')



if 'u' not in my_list :
    my_list.append('u')

print(my_list)



# append ile birden fazla elemanı listin sonuna ekleme :

a = ["apple", "banana", "cherry"]

a.append("Ford", "BMW", 5)

print(a)

# TypeError: list.append() takes exactly one argument 
# Bu şekilde birden fazla eleman eklemeye çalışırsanız hata alırsınız...
# append() argument olarak sadece bir eleman alır.

a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a)


a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

for element in b :
    a.append(element)

print(a)



# extend() :
# extend() methodu ile birden fazla elemanı başka bir list'e doğrudan tek seferde ekleyebiliriz :
# extend() methodu argument olarak bir list alabilir. Eklemek istediğiniz tek bir elemanı 
# veya birden fazla elemanı bir list içerisinde extend methoduna vereblirsiniz.
# Veya birden fazla elemana sahip bir string de verebilirsiniz, stringin her bir karakterini 
# ayrı bir eleman olarak ekler.

# Syntax ;  my_list.extend(iterable_object)

a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.extend(["Lenovo"])

print(a)

# insert()

# Bir list'te istenilen lokasyona index numarası belirtilerek eleman eklemeyi sağlar.

# argument olarak index numarasını ve obje alır.

# Syntax ;    insert(index, object)

nums = [1,2,3,4]
nums.insert(0, 5)

nums.insert(3, "two-and-half")
print(nums)


a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]
index_num = 1
for element in b :
    a.insert(index_num, element)
    index_num = index_num + 1

print (a)


# LIST YAPILARINDAN ELEMAN SİLME METHODLARI :

# remove() methodu :
# silinmek istenilen objeyi doğrudan argument olarak gireriz.
# Yalnızca tek bir eleman alır birden fazla girerseniz hata alırsınız.

nums = [1,2,3,4]

nums.remove(3)

print(nums)


# pop() methodu :

# silinmek istenilen objenin index numarasını argument olarak alır.
# Hiçbir index numarası girmezseniz default olarak list'in en sonundakini siler.
# Yalnızca tek bir index nosu alır birden fazla girerseniz hata alırsınız.

nums = [1,2,3,4]
nums.pop(0)

print(nums)


help(list)
help(list.append)



#list.clear()
# list içerisindeki tüm elemanları siler...

my_list = [2, 3, 5, 7, 11, 13] 

my_list.clear()
print(my_list)



# list.sort(key=None, reverse=False)
# sort() methodu geriye bir değer döndürmez.
my_list = [5, 3, 6, 1, 2, 4, 7]
my_list.sort()

print(my_list)

a_list = [1, 5, 67, 3, 4]

x = a_list.sort()

print(x)
print(a_list)


# list.reverse()
# reverse() methodu geriye bir değer döndürmez.
my_list = ["zero", "one", "two", "three", "four", "five"]

my_list.reverse()
print(my_list)



### ÇOK-BOYUTLU LİST YAPILARI - LİST'LERİN LİST'İ 

my_course = [ ["Ahmet", 90, 85, 70], ["Mehmet", 76, 87, 55], ["Ali", 43, 71, 93] ]

#print(my_course[1])

#print(my_course[1][2])

x = my_course[1]

z = x[2]

# print(x, z)

y = my_course[2][0]    # y = "Ali"
t = y[0]               # t = 'A'
n = my_course[2][0][0]  # n = 'A'
# y = "Ali"

"""
