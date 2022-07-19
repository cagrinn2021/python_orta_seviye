#clasin dısaridan erisime engelleme, istenmeyen verilerin degisistirilmemesi
##methotlarda __add__ oldugunda bu alt tire korumali oldugunu gostermektedir

class memur:
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.__maas=maas
        self.__zam=0.20

    def zamorani(self):
        self.__maas=self.__maas*self.__zam+self.__maas

    def getmaas(self):
        return self.__maas
    def getzam(self):
        return self.__zam
    def setzam(self,yenioran):
        self.__zam=yenioran

memur1=memur("cagri","esen",20000)
print(memur1.ad)
print(memur1.soyad)
# print(memur1.maas) #class icinde __ koyduguumuz icin erisimi kısıtladık ve bu bulunamıyor
# print(memur1.zam)
##yukarda erisemiyorduk ama clasin icinde get olusturduk ve bu sayede veriyi görebilir hale geldik
print(memur1.getmaas())
print(memur1.getzam())
#simdi degisiklik yapmak istersek ne yapabiliriz bunu gorelim

memur1.setzam(0.5)
memur1.zamorani()
print(memur1.getmaas())