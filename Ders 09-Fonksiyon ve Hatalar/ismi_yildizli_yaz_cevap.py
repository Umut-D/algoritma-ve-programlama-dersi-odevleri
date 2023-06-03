# 1 ila 49 arasında 6 farklı değer oluşturan ve bunu dizi olarak geri döndüren bir fonksiyon yazınız
import random

def sayisal_loto():
    sayilar = []
    while len(sayilar) != 6:
        rastgele_sayi = random.randint(1, 50)
        if not (rastgele_sayi in sayilar):
            sayilar.append(rastgele_sayi)

    return sayilar