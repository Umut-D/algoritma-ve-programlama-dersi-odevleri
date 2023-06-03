# Gereksinimleri düşünüp Üçgen ve Çember sınıflarını oluşturup hesaplamalar yapınız
import math


class Cember:
    def hesapla(self, yaricap):
        return math.pi * (yaricap ** 2)


class Ucgen:
    def __init__(self, taban, yukseklik):
        self.taban = taban
        self.yukseklik = yukseklik

    def hesapla(self):
        return self.taban * self.yukseklik / 2


cember = Cember()
sonuc = cember.hesapla(5)
print(f"Çember Alan: {round(sonuc, 3)}")

ucgen = Ucgen(3, 3)
sonuc = ucgen.hesapla()
print(f"Üçgen Alan: {round(sonuc, 3)}")
