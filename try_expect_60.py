try:
    x = int(input("lütfen ilk sayi giriniz"))
    y = int(input("lütfen ikinci sayi giriniz"))

    print(x / y)
# except ZeroDivisionError:
#     print("Sifira bolmeye calistin bro")
# except ValueError:
#     print("sayi disinda bir deger girdiniz")

#boyle tek tek girilemez

# except (ZeroDivisionError,ValueError):
#     print("hatali bir deger girdiniz ") ##boyle de yapabiliriz

# except:
#     print("bir seyi yanlis yaptin")
# else:
#     print("sorunsuz calistirildi")



except Exception as hata:
    print("bi sorun var ===",hata)
