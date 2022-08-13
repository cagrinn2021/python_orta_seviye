import random

x=random.random()# 0 ile 1 arasında rastgele sayi üretir
print(x)
x=random.uniform(1,20)# girilen değerler arasinda rastgele sayilar üretilir
print(x)
x=random.randint(1,20)#girilen değerler arasinda tam sayi olarak üretir
print(x)

y=["ali","cagri","emre","sebo","cagla"]
x=random.choice(y)# rastgele seçim yapabiliyoruz bir dizi içinde
print(x)

y="Merhaba"
x=random.choice(y)
print(x)


liste=range(0,100)
x=random.sample(liste,5)
print(x)