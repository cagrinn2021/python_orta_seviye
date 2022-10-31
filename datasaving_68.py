import re
import time
class Kayıt:
    def __init__(self,programad):
        self.programad=programad
        self.dongu=True
    def program(self):
        secim=self.menu()
        if secim =="1":
            print("kayit ekleme menüsüne yönlendiriliyorsunuz")
            time.sleep(3)
            self.kayıtekle()
        if secim=="2":
            print("kayit silme menusune yönlendiriyorsunuz")
            time.sleep(3)
            self.kayıtcıkar()
        if secim=="3":
            print("verileri erisiliyor")
            time.sleep(3)
            self.kayıtoku()
        if secim=="4":
            self.cıkıs()
    def menu(self):
        def kontrol(secim):
            if re.search("[^1-4]",secim):
                raise Exception("lütfen 1 ve 4 arasi girin")
            elif len(secim)!=1:
                raise Exception("lütfen 1 ve 4 arasi girin")
        while True:
            try:
                secim=input("Merhabalar, {} otomasyon sistemine hoşgeldiniz\n\nYapmak istediğiniz işlemi seçin\n1=Kayıt Ekle\n2=Kayıt Sil\n3=Kayıt Oku\n4=Cikis".format(self.programad))
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim


    def kayıtekle(self):
        def kontrolad(Ad):
            if Ad.isalpha()==False:
                raise Exception("adiniz sadece alfabetik olmalidir")
        while True:
            try:
                Ad=input("Adiniz: ")
                kontrolad(Ad)
            except Exception as hataad:
                print(hataad)
                time.sleep()
            else:
                break
        def kontrolsoyad(Soyad):
            if Soyad.isalpha()==False:
                raise Exception("Soyadiniz sadece alfabetik olmalidir")
        while True:
            try:
                Soyad=input("SoyAdiniz: ")
                kontrolad(Ad)
            except Exception as hatasoyad:
                print(hatasoyad)
                time.sleep(3)
            else:
                break

        def kontrolyas(Yas):
            if Yas.isdigit() == False:
                raise Exception("Yasiniz sadece Sayi olmalidir")

        while True:
            try:
                Yas = input("Yasiniz : ")
                kontrolyas(Yas)
            except Exception as hatayas:
                print(hatayas)
                time.sleep(3)
            else:
                break
        def kontroltc(Tc):
            if Tc.isdigit() == False:
                raise Exception("Sadece rakam olmalidir")
            elif len(Tc)!=11:
                raise Exception("Kimlik No 11 Hane olmali")
        while True:
            try:
                Tc = input("Tc : ")
                kontroltc(Tc)
            except Exception as hatatc:
                print(hatatc)
                time.sleep(3)
            else:
                break
        def kontrolmail(Mail):
            if not re.search("@" and ".com",Mail):
                raise Exception("Gecersiz mail")
        while True:
            try:
                Mail= input("Mailiniz: ")
                kontrolmail(Mail)
            except Exception as hatamail:
                print(hatamail)
                time.sleep(3)
            else:
                break
        with open("C:/Users/cagri/OneDrive/Masaüstü/Bilgiler.txt","r",encoding="utf-8") as Dosya:
            satırsayisi=Dosya.readlines()
        if len(satırsayisi)==0:
            Id=1
        else:
            with open("C:/Users/cagri/OneDrive/Masaüstü/Bilgiler.txt", "r", encoding="utf-8") as Dosya:
                Id=int(Dosya.readlines()[-1].split("-")[0])+1
        with open("C:/Users/cagri/OneDrive/Masaüstü/Bilgiler.txt", "a+", encoding="utf-8") as Dosya:
            Dosya.write("{} {} {} {} {} {} \n".format(Id,Ad,Soyad,Yas,Tc,Mail))
            print("Veriler işlenmiştir...")
            self.menudon()

Sistem=Kayıt("Cagriiii")
while Sistem.dongu:
    Sistem.program()
