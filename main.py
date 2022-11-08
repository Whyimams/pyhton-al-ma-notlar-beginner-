import random 
import math

kucuksayi=int(input("KÜÇÜK SAYIYI GİRİNİZ:"))
buyuksayi=int(input("BÜYÜK SAYIYI GİRİNİZ:"))

x= random.randint(kucuksayi,buyuksayi)

print("\n\t Sadece ",
	round(math.log(buyuksayi - kucuksayi + 1, 2)),
	" kadar deneme şansınız vardır! \n")

count=0

while count<math.log(buyuksayi-kucuksayi+1,2):
  count=+1

  guess= int(input("Tahmin ediniz="))

  if guess==x :
    print("TEBRİKLER!",count,"Deneme")

    break
  elif x>guess:
    print("Sayınız çok küçük!")
  elif x<guess:
    print("sayınız çok büyük")


if count>=math.log(buyuksayi-kucuksayi+1,2):
  print("\n Sayı : %d" % x)
print("\tBir sonraki denemenizde bol şans")