# Ödevde kullanılan modülü içe aktaralım
import harf_frekans_modulu

# Kullanıcıdan metin girişi istenir.
text = input("Lütfen metni girin: ")

# Kendisine gönderilen metinde harflerin kullanım sıklığını (yüzdelik oranını) bulan fonksiyon
print(harf_frekans_modulu.calculate_frequency(text))

# Kendisine gönderilen karakterin bir harf olup olmadığını bulan fonksiyon
print(harf_frekans_modulu.is_letter(text[0]))

# Modülün içindeki bilgileri ekrana yazdırır.
harf_frekans_modulu.print_info()