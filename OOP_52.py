class musteri():
    def __init__(self,ad,soyad,kartsifre,hesapbakiye,kredikartiborc,sonodeme):
        self.ad=ad
        self.soyad=soyad
        self.hesapbakiye=hesapbakiye
        self.kredikartiborc=kredikartiborc
        self.sonodeme=sonodeme
        self.kartsifre=kartsifre
Ahmethesap=musteri("ahmet","Candan","1234",5000,4000,"11/12/2022")
Mehmethesap=musteri("mehmet","Can","1423",1234,2000,"21/02/2022")
takilankart=Ahmethesap

class atm():
    def __init__(self,atmad):
        self.atmad=atmad
        self.giriskontrol()
        self.dongu=True

    def giriskontrol(self):
        hak=2
        for i in range(0,3):
            sifre=input("lütfen 4 haneli sifrenizi giriniz")
            if sifre==takilankart.kartsifre:
                self.program()
            elif sifre!=takilankart.kartsifre and hak!=0:
                print("Hatali sifre girdiiniz kalan hakkiniz {}".format(hak))
                hak-=1
            elif sifre!=takilankart.kartsifre and hak==0:
                print(""" Sifrenizi yanlıs girdiniz\n kartınız bloke olmustur\n en yakın bankaya gidiniz""")
                exit()

    def program(self):
        secim=self.menu()
        if secim==1:
            self.bakiye()
        if secim==2:
            self.kkborc()
        if secim==3:
            self.paracek()
        if secim==4:
            self.parayatir()
        if secim==5:
            self.cikis()
        else:
            print("lütfen gecerli bir sayi giriniz")

    def menu(self):
        secim=int(input("""Merhaba hosgeldiniz {} Banka hoşgeldiniz
        Sayın {} {}
        Lutfen yapmak istediginiz işlemi seçiniz
        [1]Bakiye Sorgulama
        [2]Kredi Kartı Borç sorgulama
        [3]Para Çekme
        [4]Para Yatirma
        [5]Kart İade""".format(self.atmad,takilankart.ad,takilankart.soyad)))
        while secim<1 or secim>5:
            print("lütfen gecerli deger giriniz")
            self.program()
        return secim

    def bakiye(self):
        print("Hesap bakiyeniz {}".format(takilankart.hesapbakiye))
        self.dongu=False
        self.menudon()

    def menudon(self):
        x=int(input("""ana menüye dönmek icin lütfen 7 tusuna basin
        kart iade iciin 5e bas"""))
        if x==7:
            self.program()
        elif x==5:
            self.cikis()

    def kkborc(self):
        print("Kredi kartı borcunuz ={}, Son ödeme tarihiniz{}".format(takilankart.hesapbakiye,takilankart.sonodeme))
        self.dongu=False
        self.menudon()

    def paracek(self):
        miktar=int(input("lütfen cekigenizi degeri giiriniz"))

        if miktar>takilankart.hesapbakiye:
            print("yetersiz bakiye")
            self.menudon()
        else:
            yenimiktar = takilankart.hesapbakiye - miktar
            print("lütfen paranizi aliniz kalan tutar  {}".format(yenimiktar))
            self.menudon()
            yenimiktar = takilankart.hesapbakiye - miktar

    def parayatir(self):
        miktar2=int(input("lütfen yatırılcak tütari giriniz"))
        yenimiktar2=miktar2+takilankart.hesapbakiye
        print("yatırma işlemi başarı ile güncel tutar {}".format(yenimiktar2))
        self.menudon()

    def cikis(self):
        print("iyi günler")
        self.dongu=False
        exit()


banka=atm("xBank")

while banka.dongu():
    banka.program()