# İsim, Bölüm, Maaş bilgilerinin olduğu bir personel sınıfı oluşturup, 2 yönetim, 1 muhasebe ve lojistik bölümü
# çalışanları ekleyin. Bunların maaşlarına %10 zam yapan fonksiyon ekleyin. Bu sınıfı çağırın ve işlemleri yaptırın


class Personel:
    def __init__(self, isim, bolum, maas):
        self.isim = isim
        self.bolum = bolum
        self.maas = maas

    def zam_hesapla(self):
        hesap = self.maas + (self.maas * (10 / 100))
        return round(hesap)


ali = Personel("Ali", "Yönetim", 10000)
ece = Personel("Ece", "Yönetim", 12000)
efe = Personel("Efe", "Muhasebe", 13000)
zeynep = Personel("Zeynep", "Lojistik", 14000)

personeller = [ali, ece, efe, zeynep]

for personel in personeller:
    print(f"Personel Ad: {personel.isim}, Bölüm: {personel.bolum}, Zamlı Maaş: {personel.zam_hesapla()}")
