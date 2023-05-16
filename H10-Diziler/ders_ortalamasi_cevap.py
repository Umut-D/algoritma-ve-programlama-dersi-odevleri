# Bir dizi içerisinde verilen notların ortalamasını alın
fen_notlari = [10, 80, 25, 78, 84, 33, 44, 100, 5, 49, 36, 67, 75]
ogrenci_sayisi = len(fen_notlari)
sinif_ortalamasi = round(sum(fen_notlari) / ogrenci_sayisi, 3)
print(sinif_ortalamasi)