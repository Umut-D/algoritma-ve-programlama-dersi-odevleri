# N defa adınızı yazın
def tekrarla(kelime, tekrar_sayisi):
    # Eğer kelime harflerden oluşuyorsa ve boş değilse gerekli işlemi yap
    # Bu sayede try-except kullanmaktan yırttık
    if kelime.isalpha() and not len(kelime) == 0:
        for sayi in range(tekrar_sayisi):
            print(kelime)