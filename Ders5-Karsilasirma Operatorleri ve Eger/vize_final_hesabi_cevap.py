# Vizenin %40'ı, finalin %60'ını alarak geçti-kaldı yazdır (Operatör zincirleme ile yapın)

# Notları al
vize = float(input("Vize notunu girin: "))
final = float(input("Final notunu girin: "))

# Vize ve final aralıklarını metot zincirleme yaparak belirt
vize_araligi = 0 <= vize <= 100
final_araligi = 0 <= final <= 100

sonuc = 0
if vize_araligi and final_araligi:
    # Hesaplama işlemlerini yap
    sonuc = (vize * 0.4 + final * 0.6)
    print("Sonuç", sonuc)
else:
    print("Girilen değerler 0 ve 100 arası olmalıdır")