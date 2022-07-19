# classin icinde fonksiyon yaratiyorsak buna metot denilir eger classin icinde degilse fonksiyon denilir
class insan:
    def __init__(self,ad,soyad,dogumyil):
        self.ad=ad
        self.soyad=soyad
        self.dogumyil=dogumyil
    def bilgi(self):
        print("merhaba benim ismim {}, soyadım {}, dogum yilim {}".format(self.ad,self.soyad,self.dogumyil))
    def yas(self):
        return 2022-self.dogumyil

insan1=insan("cagrii","esen",1996)
insan2=insan("sukran","esen",1970)

insan1.bilgi()
insan2.bilgi()

print(insan1.yas())