# Girilen dizideki sayıların ortalamasını alıp döndürün

def ortalama_bul(sayilar):
    try:
        ortalama = sum(sayilar) / len(sayilar)
        return ortalama
    except (TypeError, ValueError, ZeroDivisionError):
        # Dizide sayı harici bir karakter girilirse TypeError hatası döner
        return "Çok yanlış hatalar dönüyor"