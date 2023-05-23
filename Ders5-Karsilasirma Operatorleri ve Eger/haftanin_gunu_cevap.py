# Haftanın hangi günü olduğunu bulan bir yapı oluşturun (Kontrol mekanizmalı yapın)
deger = int(input("Haftanın kaçıncı günü: "))

# Değer kontrolü yap ve günü yazdır
gun = ""
if 1 <= deger <= 7:
    if deger == 1:
        gun = "Pazartesi"
    elif deger == 2:
        gun = "Salı"
    elif deger == 3:
        gun = "Çarşamba"
    elif deger == 4:
        gun = "Perşembe"
    elif deger == 5:
        gun = "Cuma"
    elif deger == 6:
        gun = "Cumartesi"
    elif deger == 7:
        gun = "Pazar"
    print(f"Haftanın {deger}. günü, {gun}")
else:
    # Aralık harici veri girildiğinde hata ver
    print("Lütfen 1-7 arası değer giriniz!")