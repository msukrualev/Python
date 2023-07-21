######### Bir kelimenin içindeki sesli harfleri bulan programdır... #########

sesliler = ['a', 'e', 'i', 'o', 'u']

kelime = "TechProeducation"

found = []

for harf in kelime :
    if harf in sesliler :
        if harf not in found :
            found.append(harf)

for sesli_harf in found :
    print(sesli_harf)