# Her bir sayı ve karesini programlamatik olarak oluşturup bunları tek tek yazdırın

sozluk = {}
for sayi in range(1, 51):
    sozluk[sayi] = sayi * sayi

for sayi, us in sozluk.items():
    print(sayi, us, sep=":")