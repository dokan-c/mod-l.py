# Kendisine gönderilen karakterin bir harf olup olmadığını bulan fonksiyon
def is_letter(char):
    if char.isalpha():
        return char.isalpha()

# Kendisine gelen harfi (büyükse) küçük harfe çeviren bir fonksiyon
def to_lower(char):
    return char.lower()

# Kendisine gönderilen metinde harflerin kullanım sıklığını (yüzdelik oranını) bulan fonksiyon
def calculate_frequency(text):
    text = text.lower()
    total_characters = len(text)
    frequency = {}
    
    for char in text:
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
                
    for char, count in frequency.items():
        frequency[char] = (count / total_characters) * 100
        
    return frequency

# Modül çağırıldığında ekrana çıktı olarak veren fonksiyon
def print_info():
    print("Ad: Doğukan")
    print("Soyad: CEBECİ")
    print("Öğrenci Numarası: 211213111")
    print("Not: Merhabalar!")