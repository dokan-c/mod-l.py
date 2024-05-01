import sqlite3
import Levenshtein

conn = sqlite3.connect("texts.db")
c = conn.cursor()


c.execute("""
    CREATE TABLE IF NOT EXISTS Texts (
        id INTEGER PRIMARY KEY,
        text_content TEXT
    )
""")

text1 = input("İlk metni girin: ")
text2 = input("İkinci metni girin: ")

c.executemany("INSERT INTO Texts (text_content) VALUES (?)", [(text1,), (text2,)])

conn.commit()

conn.close()

lev_distance = Levenshtein.distance(text1, text2)
max_len = max(len(text1), len(text2))
similarity_ratio = (1 - lev_distance / max_len) * 100

report = f"İlk metin: {text1}\nİkinci metin: {text2}\nBenzerlik oranı: {similarity_ratio:.2f}%\n"

with open("benzerlik_durumu.txt", "w") as f:
    f.write(report)
print(report)
print("Benzerlik durumu 'benzerlik_durumu.txt' dosyasına yazıldı.")

#Benzerliği Levenshtein Yöntemi İle Bulduk.