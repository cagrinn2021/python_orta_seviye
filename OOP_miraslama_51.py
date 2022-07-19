class insan():
    def __init__(self,ad,soy,sacrengi,boy,kilo):
        self.ad=ad
        self.soy=soy
        self.sacrengi=sacrengi
        self.boy=boy
        self.kilo=kilo

class ogrenci(insan):
    def __init__(self,ad,soy,sacrengi,boy,kilo,bolum,yas):
        super().__init__(ad, soy, sacrengi, boy, kilo)
        self.bolum=bolum
        self.yas=yas
    def getall(self):
        print("{},{},{},{},{},{},{}".format(self.ad,self.soy,self.sacrengi,self.boy,self.kilo,self.bolum,self.yas))

insan1=insan("cagri","esen","siiyah",1.78,74)
print(insan1.ad)
ogrenci1=ogrenci("ahmet","tepe","kahve",1.78,74,"elektronik",26)
ogrenci1.getall()