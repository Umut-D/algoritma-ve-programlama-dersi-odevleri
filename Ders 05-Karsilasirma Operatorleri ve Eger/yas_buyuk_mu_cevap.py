# Web sitesine girerken yaş kontrolü yapınız (18'den büyük mü)

# Kullanıcının yaşını al
girilen_yas = 19

# Koşullara göre dallan
if girilen_yas < 18:
    mesaj = "Siteye giriş yapamazsınız. Yaşınız 18'den küçük"
else:
    mesaj = "Hoşgeldiniz."

# Sonucu yazdır
print(f"Durum: {mesaj}")