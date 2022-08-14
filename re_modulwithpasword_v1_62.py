import re
dogumtarihi="1998"
# karakter=["\?","\*","\!","\%"]
karakter=["\?"]
def sifrekontrol(sifre):
    if len(sifre)<8:
        raise Exception("En az sekiz tane karakterli olmalı")
    elif not re.search("[a-z]",sifre):
        raise Exception("En az bir tane kücük harf olmalı")
    elif not re.search("[A-Z]",sifre):
        raise Exception("lEn az bir tane büyük harf olmalı")
    elif not re.search("[0-9]",sifre):
        raise Exception("En az bir tane rakam olmalı")
    elif not re.search(str(karakter,sifre)):
        raise Exception("En az bir tane özel karekter olmalı (?,*,!,%)")
    elif sifre.startswith(dogumtarihi)==True:
        raise Exception("dogum tarihi ile başlayamaz")
    elif sifre.endswith(dogumtarihi)==True:
        raise Exception("dogum tarihi ile bitemez")
    else:
        print("sifreniz olusturulmustur")

while True:
    try:
        sifre=input("lütfen sifrenizi olusturunuz")
        sifrekontrol(sifre)
    except Exception as hata:
        print(hata)
    else:
        break
