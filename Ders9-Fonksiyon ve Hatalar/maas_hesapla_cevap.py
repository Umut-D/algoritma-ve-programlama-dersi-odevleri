# 3 farklı personel için zamlı maaşları hesaplayan bir fonksiyon yazın
# Her bir personelin 10.000 aldığını temel alarak, Ahmet'in %10, Ece'nin %12, Nihat'ın %15 zamlı maaşlarını hesaplayın

def zamli_maas_hesapla(ad, oran):
    SABIT_MAAS = 10000

    # Öncelikle zamlı oranları hesapla
    zam_farki = (SABIT_MAAS * (oran / 100))

    # Zam farkını sabit maaş üzerine koyarak zamlı maaş oranını bul
    zamli_maas = round(SABIT_MAAS + zam_farki)
    print(f"{ad} adlı personelin zamlı zaaşı: {zamli_maas}")