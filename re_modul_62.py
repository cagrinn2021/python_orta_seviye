#re modülü regular explasion her hangi bir karekter yapısı içinde bir veri arama ve düzenleme için kullanılır
import re

x="merhaba, benim adim cagri"
y=re.findall("merhaba",x)#ne arıcağı ve nerede arıcağını yazıyoruz
print(y)#eğer var ise listeyi döndürüyor eğer yoksa boş liste döndürüyor

y=re.split(" ",x)# kritere göre listeyi parçaladı
print(y)

y=re.sub("a","A",x)#ilki hangi harfi, ikinci harfi neyle değiştirceği, üç nerede yapıcağı
print(y)
y=re.search("merhaba",x)
print(y)
print(y.span())
print(y.start())
print(y.end())
print(y.string)#nerede aradiğimizi gösteriyor
y=re.findall("[c-g]",x)#aralikta aramak yapmak istiyorsak
print(y)
y=re.findall("[^c-g]",x)#bu harfleri dışlayarak arama yappıyor
print(y)
y=re.findall("^m",x)#aranilan yerin ilk harfini soruyoruz
print(y)#bulursa değeri ilste olarak gönderiyor bulamazsa boş
y=re.findall("i$",x)#yapilan yerinin son yerine bakıyor
print(y)#bulursa değeri ilste olarak gönderiyor bulamazsa boş
y=re.findall("\s",x)#boşluk arayan yer
print(y)#bulursa gösterir