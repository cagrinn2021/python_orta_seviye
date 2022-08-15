with open("Merhaba.txt","a+") as dosya:#hem okuma hem yazma
     dosya.write("selam")
     #dosya okutmaya calısırsam burada okutmaz cünkü en son kaldığı yeerden devam eder o yüzden seek0 at
     dosya.seek(0)
     print(dosya.read())
