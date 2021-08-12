sehirler=["ankara","istanbul","izmir","hatay","ankara"]
print("ankara sayısı="+str(sehirler.count("ankara")))#count fonskıyonu lıste içindeki eleman sayısını verir
print(str(sehirler.index("ankara")))#index lıste içindeki lemanın kaçıncı indexte olduğunu veriri ancak ilk buldugunda devam etme4z 
sehirler.pop(2)#pop fonskıynu index siler
print(sehirler)
sehirler.insert(2,"izmir")#insert belirtilern indexe belirtilen elemanı ekler 

print(sehirler)
sehirler2=sehirler.copy()#copy adı uzerınde kopyalam yapar
sehirler.extend(sehirler2)#extend iki listeyi birleştirir
print(sehirler)
sehirler.sort()#sort fonksıyonu listeyi alfabetik olarak sıralar
print(sehirler)
sehirler.sort()
sehirler.reverse()#listeyi tersine çevirir
print(sehirler)