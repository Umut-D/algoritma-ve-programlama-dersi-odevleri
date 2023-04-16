# 1'den n'ye kadar olan sayıları topla
ust_deger = int(input("Kaça kadar toplam olsun: "))
toplam = 0

# Her bir döngüde toplama ekleme yap
for deger in range(ust_deger + 1):  # Toplama, girilen sayıyı da dahil et
    toplam += deger
print("TOPLAM: ", toplam)