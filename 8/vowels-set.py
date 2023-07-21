######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########

# sesliler = ['a', 'e', 'i', 'o', 'u']

sesliler = set('aeiou')

kelime = input("Sesli harf aranacak kelimeyi giriniz: ")

# found = []
"""
for harf in kelime :
    if harf in sesliler :
        if harf not in found :
            found.append(harf)
"""
found = sesliler.intersection(set(kelime))

for sesli_harf in found :
    print(sesli_harf)