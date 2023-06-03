# Girilen plaka koduna denk gelen şehri yazdırın

plaka_kodlari = tuple(range(1, 82))
sehirler = ("Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir",
            "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli",
            "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum ", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane",
            "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli",
            "Kırşehir", "Kocaeli", "Konya", "Kütahya ", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş",
            "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat",
            "Trabzon  ", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt ", "Karaman",
            "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük ", "Kilis", "Osmaniye ",
            "Düzce")

girilen_plaka_kodu = 34

# Zip ile iki ayrı demeti birleştir ve anahtar-değer (key-value) şeklinde sözlüğe dönüştür
plaka_ve_sehir = dict(zip(plaka_kodlari, sehirler))

# Hata mesajı da barındıran sonucu değişkene ata ve yazdır
sozluge_gore_sonuc = plaka_ve_sehir.get(girilen_plaka_kodu, "Böyle bir plaka kodu bulunamadı")
print(f"{girilen_plaka_kodu} plaka kodlu şehir: {sozluge_gore_sonuc}")