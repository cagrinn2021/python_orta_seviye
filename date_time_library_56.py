from datetime import*
import time
## eğer * kullanmasaydik aşağıda datetime.datetime.now() olarak kullancaktık aynı isimde fonksiyon var ondan=
x=datetime.now()
print(x)
x=datetime.today()
print(x.strftime("%d-%m-%y"))
x=datetime.today()
print(x.minute)
x=date(1111,11,3)
print(x)

x=datetime.now()
y=datetime.ctime(x) ## günü ayı tarihi saati ve yılı söylüyor
print(y)

#

bugun=datetime.today()
fark=timedelta(days=5550)
gecmis=bugun-fark
print(gecmis)


while True:
    zaman=time.strftime("%H:%M:%S")
    print(zaman)
    time.sleep(2)
