# class Insan:
#     ad="mehmet"
#     soyad="can"
#     yas=22
#     sacrengi="siyah"
#
# print(Insan.sacrengi)
# print(Insan.ad)

##yukarida sadece sabit kisileri tanimliyor

#asagida ise istedigimiz kdar alabileceğimiz bir sınıf var self komutu bırada esleştirme yapmak icin veri almaz
class insan:
    def __init__(self,ad,soyad,yas,sacrengi):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.sacrengi=sacrengi

insan1=insan("cagri","esen",26,"kahverengi")
insan2=insan("mustafa","durmus",28,"kumral")

print(insan1.sacrengi,insan2.ad)
