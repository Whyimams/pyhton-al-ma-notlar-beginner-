import random
from typing import Counter
randomlist = []
for i in range(0,11):#burada kaç defa zar atılacağını belirtiyoruz
    n = random.randint(1,7)#zardaki yüzey sayısını belirtiyoruz
    randomlist.append(n)#çıkan random sayıları append fonksiyonu sayesınde bir listeye atıyoruz

#if else komutuna gerek kalmadan count metodu ile hangi yzüe kaç defa denk geldiğini ekrena yazdırabiliyoruz


print("Atılan Zarda 1 gelme sayısı:",randomlist.count(1))
print("Atılan Zarda 2 gelme sayısı:",randomlist.count(2))
print("Atılan Zarda 3 gelme sayısı:",randomlist.count(3))
print("Atılan Zarda 4 gelme sayısı:",randomlist.count(4))
print("Atılan Zarda 5 gelme sayısı:",randomlist.count(5))
print("Atılan Zarda 6 gelme sayısı:",randomlist.count(6))

