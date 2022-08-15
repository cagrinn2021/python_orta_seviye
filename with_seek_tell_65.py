with open("Merhaba.txt","r") as dosya:
    # dosya.seek(10)#seek kaçıncı karakterden sonra okucağını söylüyoruz
    # print(dosya.read())##burada ilk kaçı alıcağını söylüyoruz
    dosya.seek(5)
    dosya.read(11)
    print(dosya.tell())# seek ilk 5ten başla dedi sonra read ilk 11i oku dedi ve tel 16da kaldığımızı söyledi