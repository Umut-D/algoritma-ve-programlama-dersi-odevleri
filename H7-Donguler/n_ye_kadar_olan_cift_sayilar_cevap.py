# 1'dan n'ye kadar olan çift sayıları yazdır
limit = int(input("1'den kaça kadar işletilsin: "))

# Döngüyü başlatıp yazdır
for sayi in range(2, limit, 2):
    print(sayi)