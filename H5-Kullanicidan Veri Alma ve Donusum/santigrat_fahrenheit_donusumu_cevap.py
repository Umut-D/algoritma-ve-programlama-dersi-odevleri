# Santigrat>Fahrenheit dönüşümü

# Fahrenheit değerini al
celsius = int(input("Fahrenheit değerini girin: "))

# Gerekli dönüşüm formülünü bularak işlemi gerçekle
fahrenheit_donusumu = (celsius * 9 / 5) + 32

# Sonucu yazdir
print(f"{celsius} Celcius, {int(fahrenheit_donusumu)} derecedir")