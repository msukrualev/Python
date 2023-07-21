
#def harfara(ifade:str , harf:str) -> set:
    #""" ifade'deki "harf" degerlerini arar. """

#    return set(harf).intersection(set(ifade))

#print(   harfara("author", "tz")   )


def harfara(ifade:str, harf:str = 'aeiou' ) -> set:    # harf = 'fntz'
    """  ifade'deki "harf" degerlerini arar. """

    return set(harf).intersection(set(ifade))

# print (   harfara('life, the universe, and everything', 'fntz')    )

#### Positional Versus Keyword Assignment,
# Positional Assignment; argumanlara fonksiyonda tanımlı oldukları pozisyona göre deger göndermeye-atamaya denilir.
# Keyword Assignment

#print (   harfara(harf ='tfzd', ifade='life, the universe, and everything')    )

#### Call-By-Value ve Call-By-Reference farkı

def double(arg):
	print('Before: ', arg)
	arg = arg * 2
	print('After: ', arg)

def change(arg):
	print('Before: ', arg)
	arg.append('More data')
	print('After: ', arg)

# Call-By-Value örneği :
"""
num = 10

double(num)

saying = 'Hello'
double(saying)

print(num, saying)

"""
# Call-By-Reference örneği :

numbers = [ 42, 256, 16 ]
change(numbers)

print (numbers)
