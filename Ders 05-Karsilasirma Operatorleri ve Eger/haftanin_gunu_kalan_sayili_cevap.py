# Haftanın hangi günü olduğunu bulan bir yapı oluşturun (Kontrol mekanizmasız yapın - kalan sayısını kullanarak yapın)
deger = int(input("Haftanın kaçıncı günü: "))

# Değer kontrolü yap ve günü yazdır
kacinci_gun = deger % 7
gun = ""
if deger:
    if kacinci_gun == 1:
        gun = "Pazartesi"
    elif kacinci_gun == 2:
        gun = "Salı"
    elif kacinci_gun == 3:
        gun = "Çarşamba"
    elif kacinci_gun == 4:
        gun = "Perşembe"
    elif kacinci_gun == 5:
        gun = "Cuma"
    elif kacinci_gun == 6:
        gun = "Cumartesi"
    elif kacinci_gun == 0:  # En kritik nokta bu. Kalan değer 0 ile Pazar, yani 7. gün
        gun = "Pazar"
        kacinci_gun = 7  # Sonuçta 0 yazmak yerine 7 yazılmalı
    print(f"Haftanın {kacinci_gun}. günü, {gun}")