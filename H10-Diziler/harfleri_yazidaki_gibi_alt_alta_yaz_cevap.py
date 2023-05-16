# Harfleri, yazıdaki gibi alt alta yaz
durum = True
sayac = 0
while durum:
    sayac += 1
    print(adim[0:sayac])
    if len(adim) == sayac:
        durum = False