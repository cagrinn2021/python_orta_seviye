import re
import time

class kayit:
    def __init__(self,programad):
        self.programad=programad
        self.dongu=True
    def program(self):
        secim=self.menu()
        if secim=="1":
            print("kayit ekleme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)
            self.kayitekle()
        if secim=="2":
            print("kayit silme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)
            self.kayitcikar()
        if secim=="3":
            print("verilere erişiliyor")
            time.sleep(3)
            self.kayitoku()
        if secim=="4":
            self.cikis()


    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("lütfen 1 ve 4 arasinda sayi secim girin")
            elif len(secim)!=1:
                raise Exception("lütfen 1 ve 4 arasinda sayi secim giriniz")
        while True:
            try:
                secim=input("Merhaba, {} Otomasyon sistemine hoşgeldiniz\n\nYapmak istediğiniz işlemi seçim\n1=Kayıt ekle\n2=Kayit sil\n3=Kayıt oku\n4=Cikis\n\n".format(self.programad))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim





    def kayitekle(self):
        def kontrolad(ad):
            if ad.isalpha()==False:
                raise Exception("Alfabetik ad giriniz")
        while True:
            try:
                ad=input("adiniz= ")
                kontrolad(ad)
            except Exception as hataad:
                print(hataad)
                time.sleep(3)
            else:
                break

        def kontrolsoyad(soyad):
            if soyad.isalpha()==False:
                raise Exception("Alfabetik soyad giriniz")
        while True:
            try:
                soyad=input("soyad= ")
                kontrolsoyad(soyad)
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(3)
            else:
                break


        def kontrolyas(yas):
            if yas.isdigit()==False:
                raise Exception("Sayisal Deger Giriniz")
        while True:
            try:
                yas=input("yasiniz= ")
                kontrolyas(yas)
            except Exception as hatayas:
                print(hatayas)
                time.sleep(3)
            else:
                break


        def kontroltc(tc):
            if tc.isdigit()==False:
                raise Exception("Kimlik sadece sayilar olmalidir")
            if len(tc)!=11:
                raise Exception("Kimlik no 11 haneden olusmalidir")
        while True:
            try:
                tc=input("tc no= ")
                kontroltc(tc)
            except Exception as hatatc:
                print(hatatc)
                time.sleep(3)
            else:
                break

        def kontrolmail(mail):
            if not mail.search("@" and ".com",mail):
                raise Exception("gecerli bir mail giriniz")
        while True:
            try:
                mail=input("mail= ")
                kontrolmail(mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(3)
            else:
                break




    def kayitcikar(self):
        pass
    def kayitoku(self):
        pass
    def cikis(self):
        pass
    def menudon(self):
        pass


sistem=kayit("Anlasilir ekonomi")
while sistem.dongu:
    sistem.program()