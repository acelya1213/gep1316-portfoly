
from datetime import datetime  # Tarih bilgisini almak için

# Kullanıcının adını al
ad = input("Adınızı giriniz: ")

# Kullanıcının doğum yılını al
dogum_yili = int(input("Doğum yılınızı giriniz: "))

# Güncel yılı öğren
guncel_yil = datetime.now().year

# Kullanıcının yaşını hesapla
yas = guncel_yil - dogum_yili

# Kişiye özel karşılama mesajı yazdır
print(f"Merhaba {ad}!")
print(f"{yas} yaşındasınız.")
print("Python dünyasına hoş geldiniz!")
