#ilk ders hello world

message =" hello world"

print(message)
#subrstring
print(message[2])#sadece 2.indexialır
print(message[2:5])#sadece 2.indexen 5e kadar alır
print(message[2:])#2.indexten sonun kadar alır 
#len fonksıyonu
print(len(message))#ifadenın kaç inxten oluştuğunu yazdırır
#lower upper fonskıynu
print(message.upper())#messageyi büyültür
print(message.lower())#messageyı küçültür
#replace fonksıyonu
print(message.replace("h","B"))#outputta h yı b ile değiştirir
#strip split fonksiyonları 
bilgi="Beşir Alkaya 22 Hatay"
print(bilgi.split())
print(bilgi.strip())
bilgi="Beşir;Alkaya;22;Hatay"
print("Adı ="+bilgi.split(";")[0])