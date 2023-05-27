# İsimleri yıldızlı şekilde yazınız
def isimleri_yildizli_yaz(isim):
    kelime = ""
    for harf in range(1, len(isim)):
        kelime += "*"

    return isim[0] + kelime


def isimleri_yildizli_yaz_alternatif(isim):
    kalan_harf_sayisi = len(isim) - 1
    yildiz_olustur = "*" * kalan_harf_sayisi
    return isim[0] + yildiz_olustur