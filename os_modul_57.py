import os

# os.mkdir("merhaba") ##klasör olusturmak icin yazilir
# os.makedirs("merhaba/merhabaaltt")#alt dosya olusturur
# os.rename("merhaba","Xd")
# os.rmdir("Xd")

y=('C:\\Users\cagri\OneDrive\Masaüstü\okumam gereken kitaplar')

x=os.listdir(y) ##klasördekileri listeliyor
print(x)

# os.system("notepad.exe")

x=os.path.exists("1.pdf")
print(x)## eger 1.pdf var ise true döndürür yoksa false döndürür