# Girilen yazıları büyük harfle yazınız

def tekrarla(kelime):
    # Eğer kelime harflerden oluşuyorsa ve boş değilse büyük yazıp değeri döndür
    if kelime.isalpha() and not len(kelime) == 0:
        return kelime.toUpper()