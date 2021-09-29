def topla (sayi1,sayi2):
    return sayi1+sayi2
def cıkar (sayi1,sayi2):
    return sayi1-sayi2
def carp (sayi1,sayi2):
    return sayi1*sayi2
def bol (sayi1,sayi2):
    return sayi1/sayi2

print("Operasyon seçiniz")
print("1: Topla")
print("1: Çıkar")
print("1: Çarp")
print("1: Böl")

option=input("operasyon seçiniz")
sayi1=int(input("birinci sayiyi giriniz"))
sayi2=int(input("ikinci sayiyi giriniz"))

if option=='1':
    print("Toplam :"+str(topla(sayi1,sayi2)))
elif option=='2':
    print("Farkı:"+str(cıkar(sayi1, sayi2)))
elif option=='3':
    print("çarpım:"+str(carp(sayi1, sayi2)))
elif option=='4':
    print("Farkı:"+str(bol(sayi1, sayi2)))
else :
    print("gecersiz secenek ")
    
    
