# Karenin alanını hesaplayın (Negatif olursa işlemi iptal et)

# Değeri al
kenar_uzunlugu = 4

# Veri kontrolü yap. Eğer girilen veri 0'dan büyükse işlemi gerçekle
if kenar_uzunlugu > 0:
    alan = kenar_uzunlugu * kenar_uzunlugu
    print("Kenar uzunluğu", kenar_uzunlugu, "olan üçgenin alanı:", alan)
else:
    print("Girilen değer 0 veya 0'dan küçük olamaz")