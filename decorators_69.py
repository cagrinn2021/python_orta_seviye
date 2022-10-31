# #dışarıdaki fonksiyonları bir fonksiyon içinde ekleme
# def deco(func):
#     def wrapper(x,y):
#         print("işlemin sonucu..")
#         func(x,y)
#     return wrapper
# @deco
# def topla(x,y):
#     sonuc=x+y
#     print(sonuc)
# @deco
# def carpma(x,y):
#     sonuc=x*y
#     print(sonuc)
#
#
# carpma(3,2)

##veya
import time

def zamanolc(fonksiyon):
    def wrappper(*args,**kwargs):
        basla=time.time()
        time.sleep(1)
        fonksiyon(*args,**kwargs)
        bitir=time.time()
        fark=bitir-basla
        print("{} sürede çalışmasını bitirdi".format(fark))
    return wrappper
@zamanolc
def topla(x,y):
    sonuc=x+y
    print(sonuc)
@zamanolc
def carpma(x,y):
    sonuc=x*y
    print(sonuc)


topla(2,4)