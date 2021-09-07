sayi=int(input("Sayı :"))

faktoriyel =1
if sayi<0:
    print("Sayı negatıftır ve negatıf sayıların faktöriyeli yoktur!")
elif sayi==0:
    print("Sıfırın faktöriyeli 1'dir")
else :
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel*i
        
    print("Sonuç :",faktoriyel)