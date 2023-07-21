######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########
"""
sesliler = ['a', 'e', 'i', 'o', 'u']

kelime = input("Bir kelime giriniz :")   # Python

found =  []
for harf in kelime :
    if harf in sesliler :
        if harf not in found :
            found.append(harf)

for sesli_harf in found :
    print(sesli_harf)


"Techproeducation"

a : 1

e :  2

i :  1

o :  2

u :  1



sesliler = ['a', 'e', 'i', 'o', 'u']

# kelime = input("Bir kelime giriniz :")   

found = {'a':0}
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

#print(found)

#for kv in found :
#    print(kv, found[kv])

# sorted () dictionary benzeri yapılarda elamanların sıralı olarak getirilmesini saglar

#for k in sorted(found):
#    print(k, found[k])

# items()

for k, v in sorted(found.items()):
    print(k, v)


######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########
sesliler = ['a', 'e', 'i', 'o', 'u']
kelime = input("Sesli harf aranacak kelimeyi giriniz: ")

found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for harf in kelime:
    if harf in sesliler:
        found[harf] = found[harf]+1

for k, v in sorted( found.items() ):
    print(k, 'sesli harfinden', v, 'tane bulundu...')

"""
######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########
x = 3
sesliler = ['a', 'e', 'i', 'o', 'u']
kelime = input("Sesli harf aranacak kelimeyi giriniz: ")

found = {}

for harf in kelime:
    if harf in sesliler:
        found.setdefault(harf, 0)    # found['a'] = 0
        found[harf] = found[harf]+1

for k, v in sorted( found.items() ):
    print(k, 'sesli harfinden', v, 'tane bulundu...')
