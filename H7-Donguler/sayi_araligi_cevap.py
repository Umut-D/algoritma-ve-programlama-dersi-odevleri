# Girilen 2 sayının arasını yaz (örn. 80-90 arası sayıları yazdırın)

# Başlangıç ve bitiş değerlerini kullanıcıdan al (Dönüşümü unutma)
baslangic = int(input("Başlangıç sayısı: "))
bitis = int(input("Bitiş sayısı: "))

# Döngü içinde yazdır
for sayi in range(baslangic, bitis):
    print(f"{baslangic}-{bitis} arasındaki sayı: {sayi}")