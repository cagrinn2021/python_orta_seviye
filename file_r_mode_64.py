# dosya=open("Merhaba.txt","a")
# dosya.write("\ningilizce öğreneceğim, iyi kgele sana")
dosya=open("Merhaba.txt","r")
# print(dosya.read())

# for i in dosya:
#     print(i)
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())
# print(dosya.readline())## her bir satiri tek tek okuyor

# dosya2=dosya.readlines()
# print(dosya2[5])

print(dosya.read(100))
dosya.close()

