# Metre-Santimetre dönüşümü

# Kullanıcıdan verileri al
metre = input("Kaç metre? ")

# Girilen veriyi dönüştür
donusturulen_sayi = float(metre)

# İşlem yap (metre * 100)
sonuc = donusturulen_sayi * 100

# Sonucu dönüştürerek yaz (Ondalıkla uğraşmak istemedim)
print(f"Kalan: {int(sonuc)}")
