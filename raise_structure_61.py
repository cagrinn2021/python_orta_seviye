# x=int(input("lütfen bir sayi gir"))
# if x==0:
#     raise Exception("sifirdan farkli bir değer girin")
# else:
#     print(x)

def kontrol(x):
    if len(x)<5:
        raise Exception("en az 5 harfli olmali")
    else:
        print("sifreniz olusturulmustur")
x=input("bir sifre belirleyiniz")

try:
    kontrol(x)
except Exception as hata:
    print(hata)