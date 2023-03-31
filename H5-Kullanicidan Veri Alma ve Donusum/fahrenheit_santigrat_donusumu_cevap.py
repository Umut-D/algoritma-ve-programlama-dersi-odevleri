# Fahrenheit>Santigrat dönüşümü

# Fahrenheit değerini al
fahrenheit = int(input("Fahrenheit değerini girin: "))

# Gerekli dönüşüm formülünü bularak işlemi gerçekle
celsius_donusumu = (fahrenheit - 32) / 1.8

# Sonucu yazdir
print(f"{fahrenheit} Fahrenheit, {celsius_donusumu} derecedir")