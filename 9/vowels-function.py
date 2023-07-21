"""
def sesliara() :    
    sesliler = set('aeiou')
    kelime = input("Sesli harf aranacak kelime giriniz : ")
    found = sesliler.intersection(set(kelime))   
    for harf in found:
        print(harf)



def sesliara(  kelime ) :    #  kelime = "author"
    sesliler = set('aeiou')
    found = sesliler.intersection(set(kelime))   
    for harf in found:
        print(harf)

my_word = "author"

sesliara(my_word)



def sesliara(  kelime ) :    
    sesliler = set('aeiou')
    found = sesliler.intersection(set(kelime))   
    return found

def sesliara(  kelime ) :    
    sesliler = set('aeiou')
    return sesliler.intersection(set(kelime))   


found = sesliara(  "author" )

print(found)
"""
### Annotations

def sesliara(  kelime:str ) ->set :  
    """ Bir kelimedeki sesli harfleri bulur. """  
    sesliler = set('aeiou')
    return sesliler.intersection(set(kelime))   

#help(sesliara)

    